from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil, os, cv2, numpy as np
from pdf2image import convert_from_path
from insightface.app import FaceAnalysis

app = FastAPI()

os.makedirs("temp", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

face_app = FaceAnalysis(name="buffalo_l")
face_app.prepare(ctx_id=0)

@app.get("/", response_class=HTMLResponse)
def index():
    return open("static/index.html", encoding="utf-8").read()

@app.post("/verify")
async def verify(pdf: UploadFile = File(...)):
    path = f"temp/{pdf.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(pdf.file, f)

    pages = convert_from_path(path, dpi=200)

    ktp = cv2.cvtColor(np.array(pages[1]), cv2.COLOR_RGB2BGR)
    selfie = cv2.cvtColor(np.array(pages[2]), cv2.COLOR_RGB2BGR)

    f1 = face_app.get(ktp)
    f2 = face_app.get(selfie)

    if len(f1) != 1 or len(f2) != 1:
        return {"error": "Wajah tidak valid"}

    e1, e2 = f1[0].embedding, f2[0].embedding
    sim = float(np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2)))

    return {"similarity": sim, "match": sim > 0.5}
