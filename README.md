# Praktikum Teknologi Big Data - Pertemuan 1

Repository ini dibuat untuk memenuhi tugas praktikum mata kuliah **Teknologi Big Data**. Project ini mencakup instalasi ekosistem Big Data dasar menggunakan Apache Spark dan integrasi database cloud dengan MongoDB Atlas.

## 📂 Struktur Project
Sesuai dengan instruksi modul, berikut adalah struktur folder dalam project ini:
- `data/` : Berisi dataset yang digunakan dalam pemrosesan.
- `scripts/` : Berisi file python (`simple_job.py`) untuk menjalankan job Spark.
- `cloud_storage/` : Folder simulasi penyimpanan cloud.
- `README.md` : Dokumentasi project.

## 🛠️ Teknologi yang Digunakan
* **Apache Spark 3.5.0**: Engine pemrosesan data terdistribusi.
* **Python 3.14**: Bahasa pemrograman utama.
* **MongoDB Atlas**: Database cloud NoSQL untuk penyimpanan data Big Data.
* **VS Code**: Editor kode untuk pengembangan script.

## 🚀 Cara Menjalankan Script
1. Pastikan Spark sudah terinstal dan path sudah diatur di environment variables.
2. Buka terminal di VS Code.
3. Jalankan perintah berikut:
   ```powershell
   python scripts/simple_job.py
