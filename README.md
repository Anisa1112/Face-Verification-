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
