# flask-panda-kpu by devnolife

**flask-panda-kpu** adalah sebuah aplikasi web berbasis Flask yang digunakan untuk mengunggah dan membersihkan data TPS dari file Excel. Aplikasi ini memungkinkan pengguna untuk mengunggah file Excel berisi data pemilu, memilih kecamatan, kelurahan, dan memproses data sesuai dengan input pengguna.

## Fitur

1. **Unggah File Excel**: Pengguna dapat mengunggah file Excel yang berisi data TPS.
2. **Input Kode Kabupaten**: Setelah file diunggah, pengguna dapat memasukkan kode kabupaten.
3. **Pilih Kecamatan**: Sistem akan menampilkan daftar kecamatan unik yang diambil dari data Excel yang diunggah.
4. **Pilih Kelurahan**: Setelah memilih kecamatan, pengguna dapat memilih kelurahan unik dari data tersebut.
5. **Proses Pembersihan Data**: Aplikasi akan membersihkan data yang dipilih berdasarkan input pengguna dan menampilkan hasil pembersihan.

## Struktur Proyek

```bash
flask-panda-kpu/
│
├── uploads/                # Folder tempat file yang diunggah akan disimpan
├── templates/              # Folder berisi file HTML untuk tampilan
│   ├── index.html          # Halaman upload file
│   ├── input_kabupaten.html# Halaman input kode kabupaten
│   ├── input_kecamatan.html# Halaman pemilihan kecamatan
│   ├── input_kelurahan.html# Halaman pemilihan kelurahan
│   └── result.html         # Halaman untuk menampilkan hasil pembersihan data
│
├── app.py                  # File utama aplikasi Flask
├── README.md               # Dokumentasi proyek ini
└── requirements.txt        # File berisi dependensi yang diperlukan
```

## Instalasi

### Langkah-langkah:

1. **Clone repository ini**:
   ```bash
   git clone https://github.com/devnolife/flask-panda-kpu.git
   cd flask-panda-kpu
   ```

2. **Buat virtual environment (opsional tapi direkomendasikan)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk pengguna Linux/Mac
   # atau
   venv\Scripts\activate  # Untuk pengguna Windows
   ```

3. **Instal dependensi**:
   Pastikan Anda sudah menginstal `pip`. Lalu jalankan:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```

5. **Akses aplikasi**:
   Buka browser dan akses:
   ```
   http://127.0.0.1:5000/
   ```

## Penggunaan

1. **Upload File Excel**: Pilih file Excel yang berisi data TPS yang ingin Anda olah.
2. **Masukkan Kode Kabupaten**: Setelah file diunggah, masukkan kode kabupaten sesuai dengan wilayah.
3. **Pilih Kecamatan**: Sistem akan menampilkan daftar kecamatan unik dari data, pilih kecamatan yang diinginkan.
4. **Pilih Kelurahan**: Setelah memilih kecamatan, Anda dapat memilih kelurahan dari daftar yang tersedia.
5. **Lihat Hasil Pembersihan**: Setelah semua pilihan dibuat, aplikasi akan membersihkan data dan menampilkannya dalam bentuk tabel.

## Dependensi

- **Flask**: Framework Python untuk pengembangan web.
- **Pandas**: Library Python untuk manipulasi dan analisis data.
- **openpyxl**: Untuk membaca dan memanipulasi file Excel.

### Cara Menambahkan Dependensi Lain (opsional)
Jika Anda ingin menambahkan dependensi baru ke dalam proyek, Anda bisa menggunakan `pip` dan memperbarui file `requirements.txt`:
```bash
pip install <package_name>
pip freeze > requirements.txt
```

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buka *issue* atau kirim *pull request*. Semua bentuk kontribusi sangat dihargai.
