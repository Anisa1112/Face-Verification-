````md id="readmeid"
# Proyek Verifikasi Wajah Menggunakan Face Recognition untuk Validasi Bukti Pembelian Pupuk

## Overview

Proyek ini merupakan sistem verifikasi wajah menggunakan teknologi face recognition untuk memvalidasi bukti pembelian pupuk dengan cara membandingkan wajah pembeli pada foto transaksi dengan wajah yang terdapat pada Kartu Tanda Penduduk (KTP). Sistem ini dirancang untuk mencegah kecurangan dan memastikan bahwa distribusi pupuk subsidi diterima oleh pihak yang berhak.

Proses verifikasi dilakukan dengan mengambil foto pembeli saat transaksi pembelian pupuk, kemudian mencocokkannya dengan foto wajah yang diekstrak dari KTP yang diunggah. Dengan menggunakan algoritma face recognition, sistem dapat memverifikasi kesesuaian identitas sehingga meningkatkan transparansi, keamanan, dan akuntabilitas dalam proses distribusi pupuk subsidi.

Proyek ini bertujuan untuk mendukung digitalisasi verifikasi dalam program bantuan pertanian serta mengurangi risiko penyalahgunaan maupun manipulasi identitas.

---

## Fitur Utama

- Upload file PDF bukti pembelian pupuk
- Mendukung validasi melalui link URL nota transaksi
- Ekstraksi otomatis file PDF dari halaman web
- Mengambil foto KTP dan foto selfie dari PDF
- Deteksi wajah menggunakan InsightFace
- Verifikasi wajah menggunakan cosine similarity
- Validasi identitas antara foto KTP dan foto transaksi
- Preview hasil gambar untuk proses verifikasi
- Pencegahan kecurangan distribusi pupuk subsidi

---

## Teknologi yang Digunakan

### Backend
- Python
- FastAPI

### Face Recognition
- InsightFace
- FaceAnalysis (model buffalo_l)

### Image Processing
- OpenCV
- NumPy
- PDF2Image

### Library Pendukung
- Requests
- Shutil
- Regex (re)

---

## Struktur Proyek

```bash
project/
│
├── main.py
├── temp/
├── static/
│   └── index.html
│
└── README.md
````

---

## Cara Kerja Sistem

### 1. Upload Bukti Pembelian

Pengguna dapat mengunggah:

* File PDF bukti pembelian pupuk

ATAU

* Link URL transaksi yang berisi file PDF

---

### 2. Pemrosesan PDF

Sistem akan:

* Mengunduh file PDF secara otomatis
* Mengekstrak gambar dari halaman PDF
* Halaman 2 → Foto KTP
* Halaman 3 → Foto selfie pembeli

---

### 3. Deteksi Wajah

Menggunakan InsightFace:

* Mendeteksi wajah pada gambar KTP
* Mendeteksi wajah pada gambar selfie

Validasi hanya berhasil jika:

* Terdapat tepat 1 wajah pada masing-masing gambar

---

### 4. Verifikasi Wajah

Sistem membandingkan embedding wajah menggunakan cosine similarity:

```python id="simcode"
similarity = np.dot(e1, e2) / (||e1|| × ||e2||)
```

Semakin tinggi nilai similarity, semakin besar kemungkinan kedua wajah berasal dari orang yang sama.

---

## Endpoint API

## POST `/verify`

### Opsi Request

### Opsi 1 — Upload PDF

```form-data id="formpdf"
pdf: UploadFile
```

### Opsi 2 — URL PDF

```form-data id="formurl"
pdf_url: string
```

### Opsi 3 — Direct PDF URL

```form-data id="formdirect"
pdf_direct_url: string
```

---

## Contoh Response

```json id="responsejson"
{
  "source": "upload",
  "similarity": 0.87,
  "ktp_image": "/static/ktp_file.jpg",
  "selfie_image": "/static/selfie_file.jpg"
}
```

---

## Aturan Validasi

* File PDF minimal harus memiliki 3 halaman
* Foto KTP harus berada pada halaman ke-2
* Foto selfie pembeli harus berada pada halaman ke-3
* Harus terdeteksi tepat 1 wajah pada masing-masing gambar

Jika validasi gagal, sistem akan mengembalikan pesan error.

---

## Instalasi

## Clone Repository

```bash id="clonegit"
git clone https://github.com/yourusername/face-verification-project.git
cd face-verification-project
```

---

## Install Dependencies

```bash id="installdep"
pip install -r requirements.txt
```

Contoh dependencies:

```txt id="requirementstxt"
fastapi
uvicorn
opencv-python
numpy
requests
pdf2image
insightface
python-multipart
```

---

## Menjalankan Project

```bash id="runproject"
uvicorn main:app --reload
```

Buka browser:

```bash id="openbrowser"
http://127.0.0.1:8000
```

---

## Use Case

Sistem ini cocok digunakan untuk:

* Validasi distribusi pupuk subsidi
* Program bantuan pertanian
* Verifikasi identitas penerima bantuan
* Pencegahan fraud pada program subsidi pemerintah
* Monitoring digital penyaluran bantuan

---

## Manfaat Sistem

* Mengurangi penyalahgunaan identitas
* Meningkatkan akurasi verifikasi
* Menambah transparansi distribusi subsidi
* Mendukung transformasi digital sektor pertanian
* Meningkatkan akuntabilitas bantuan pemerintah

---

## Pengembangan Selanjutnya

Saran pengembangan:

* OCR untuk validasi data KTP
* Deteksi multi-face untuk mencegah fraud
* Liveness detection
* Integrasi notifikasi Telegram
* Dashboard monitoring riwayat verifikasi
* Integrasi database untuk log verifikasi

---

## Author

Dikembangkan untuk sistem verifikasi identitas digital dan validasi distribusi pupuk subsidi.

```
```
