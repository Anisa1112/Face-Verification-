# Face Verification Project menggunakan Face Recognition untuk Validasi Bukti Pembelian Pupuk

## Overview

Project ini merupakan sistem verifikasi wajah menggunakan teknologi face recognition untuk memvalidasi bukti pembelian pupuk dengan membandingkan wajah pembeli pada foto transaksi dengan wajah yang terdapat pada KTP. Sistem ini dirancang untuk mencegah kecurangan dan memastikan bahwa distribusi pupuk subsidi diterima oleh pihak yang berhak.

Prosesnya dilakukan dengan mengambil foto pembeli saat transaksi pembelian pupuk, kemudian mencocokkannya dengan wajah yang diekstrak dari KTP yang diunggah. Dengan menggunakan algoritma face recognition, sistem dapat memverifikasi kesesuaian identitas secara akurat serta meningkatkan transparansi, keamanan, dan akuntabilitas dalam proses distribusi pupuk subsidi.

Project ini bertujuan untuk mendukung digitalisasi verifikasi pada program bantuan pertanian serta mengurangi risiko penyalahgunaan atau manipulasi identitas.

---

## Fitur Utama

* Upload file PDF bukti pembelian pupuk
* Mendukung download PDF melalui link transaksi
* Ekstraksi otomatis file PDF dari halaman web
* Mengambil gambar KTP dan foto selfie dari PDF
* Deteksi wajah menggunakan InsightFace
* Verifikasi wajah menggunakan cosine similarity
* Validasi identitas antara KTP dan foto transaksi
* Menampilkan preview hasil verifikasi
* Pencegahan fraud pada distribusi pupuk subsidi

---

## Teknologi yang Digunakan

### Backend

* Python
* FastAPI

### Face Recognition

* InsightFace
* FaceAnalysis (Model buffalo_l)

### Image Processing

* OpenCV
* NumPy
* PDF2Image

### Library Tambahan

* Requests
* Shutil
* Regex (re)

---

## Struktur Project

```bash
project/
│
├── main.py
├── temp/
├── static/
│   └── index.html
│
└── README.md
```

---

## Cara Kerja Sistem

### 1. Upload Bukti Pembelian

User dapat mengirim:

* File PDF bukti pembelian pupuk

ATAU

* Link transaksi yang berisi file PDF

---

### 2. Pemrosesan PDF

Sistem akan:

* Mengunduh file PDF secara otomatis
* Mengekstrak gambar dari halaman PDF
* Halaman 2 → Gambar KTP
* Halaman 3 → Gambar selfie pembeli

---

### 3. Deteksi Wajah

Menggunakan InsightFace untuk:

* Mendeteksi wajah pada gambar KTP
* Mendeteksi wajah pada gambar selfie

Validasi berhasil jika:

* Tepat 1 wajah terdeteksi pada masing-masing gambar

---

### 4. Verifikasi Wajah

Sistem membandingkan embedding wajah menggunakan cosine similarity:

```python
similarity = np.dot(e1, e2) / (||e1|| × ||e2||)
```

Semakin tinggi nilai similarity, semakin besar kemungkinan kedua wajah adalah orang yang sama.

---

## Endpoint API

## POST `/verify`

### Pilihan Request

### Opsi 1 — Upload PDF

```form-data
pdf: UploadFile
```

### Opsi 2 — Link PDF

```form-data
pdf_url: string
```

### Opsi 3 — Direct PDF URL

```form-data
pdf_direct_url: string
```

---

## Contoh Response

```json
{
  "source": "upload",
  "similarity": 0.87,
  "ktp_image": "/static/ktp_file.jpg",
  "selfie_image": "/static/selfie_file.jpg"
}
```

---

## Aturan Validasi

* File PDF minimal terdiri dari 3 halaman
* Gambar KTP harus berada pada halaman ke-2
* Foto selfie harus berada pada halaman ke-3
* Harus terdeteksi tepat 1 wajah pada masing-masing gambar

Jika validasi gagal, sistem akan menampilkan pesan error.

---

## Instalasi Project

## Clone Repository

```bash
git clone https://github.com/yourusername/face-verification-project.git
cd face-verification-project
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Contoh isi requirements.txt:

```txt
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

```bash
uvicorn main:app --reload
```

Buka browser:

```bash
http://127.0.0.1:8000
```

---

## Use Case

Sistem ini cocok digunakan untuk:

* Verifikasi distribusi pupuk subsidi
* Program bantuan pertanian
* Validasi identitas penerima bantuan
* Pencegahan fraud pada program subsidi pemerintah
* Sistem monitoring dan akuntabilitas digital

---

## Manfaat

* Mengurangi penyalahgunaan identitas
* Meningkatkan akurasi verifikasi
* Menambah transparansi distribusi subsidi
* Mendukung transformasi digital sektor pertanian
* Meningkatkan akuntabilitas program bantuan pemerintah

---

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

* OCR untuk validasi data KTP
* Deteksi multi-face untuk mencegah manipulasi
* Liveness detection
* Integrasi notifikasi Telegram
* Dashboard monitoring riwayat verifikasi
* Integrasi database untuk penyimpanan log verifikasi

---

## Author

Dikembangkan untuk sistem verifikasi identitas digital dan validasi distribusi pupuk subsidi.
