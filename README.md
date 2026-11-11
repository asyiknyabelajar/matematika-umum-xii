# MATEMATIKA UMUM XII — PENDAMPING AKADEMIK

Satu halaman Blogger, seluruh isi disimpan dan disajikan dari GitHub Pages. **Ini Matematika Umum, bukan Matematika Tingkat Lanjut.** Berdasarkan 4 bab buku pemerintah edisi revisi 2025. Terdapat 26 subbab, 52 materi dengan analogi, pemahaman C2, contoh C3, analisis C4, proyek C5, dan rekam progres lokal.

## 1. Unggah ke GitHub

1. Masuk ke akun GitHub `asyiknyabelajar`.
2. Pilih **New repository**. Beri nama **`matematika-umum-xii`**, pilih **Public**, lalu **Create repository**.
3. Pilih **Add file → Upload files** dan unggah **`index.html`**, **`style.css`**, **`app.js`**, dan **`materi.js`** langsung ke **root repository**, bukan ke folder bersarang.
4. Pilih **Commit changes**.
5. Buka **Settings → Pages → Build and deployment**. Source **Deploy from a branch**, branch **main**, folder **/(root)**, lalu **Save**.
6. Coba akses `https://asyiknyabelajar.github.io/matematika-umum-xii/` setelah GitHub Pages selesai terbit. URL tersebut **belum otomatis aktif hanya karena paket dibuat**.

> Untuk mengedit konten, file `materi.js` dapat diedit sebagai data JavaScript. File `materi.json` disertakan sebagai format baca yang nyaman, dan `build_content.py` sebagai naskah pembangkit asli 52 pelajaran. Jika mengedit `materi.json` saja, jalankan langkah pembaruan di bawah untuk membentuk ulang `materi.js` sebelum unggah.

## 2. Pasang di SATU halaman Blogger

1. Blogger → **Halaman** → **Halaman Baru**.
2. Masukkan judul dari `JUDUL_DAN_SEO.txt`.
3. Pilih mode tampilan **HTML** (bukan Compose).
4. Salin **semua isi** file `KODE_BLOGGER.html` ke editor HTML.
5. Gunakan **Pengaturan → Deskripsi penelusuran** dengan teks dari file SEO.
6. **Publikasikan**. Hanya perlu satu halaman Blogger untuk seluruh 4 bab.

Jika nama akun atau repository berbeda dari contoh, ubah **kedua** URL `https://asyiknyabelajar.github.io/matematika-umum-xii/` di `KODE_BLOGGER.html` sesuai alamat GitHub Pages yang sesungguhnya.

## 3. Fungsi pembelajaran

- **Bab > subbab > materi:** daftar isi serta pencarian yang langsung membuka isi yang dipilih.
- **Kembali, sebelumnya, lanjut:** navigasi tanpa membuat halaman Blogger baru.
- **Kuis C2:** pilihan jawaban dengan penjelasan benar/salah.
- **Contoh C3:** perhitungan bertahap dan satuan hasil.
- **C4:** pertanyaan analisis pada akhir setiap subbab (jawaban terbuka, tidak dinilai otomatis).
- **C5:** proyek pada bagian akhir tiap bab (evaluasi dan penyelidikan kelompok).
- **Kemajuan:** tombol *Tandai materi selesai*, penanda dibaca dan progress bar. Disimpan sebagai `localStorage`, **hanya di browser/perangkat yang sama** dan tidak sinkron dengan akun siswa.
- **Foto nyata:** 4 foto Unsplash berbeda, dimuat dari URL online (bukan gambar flat atau ilustrasi buatan). Jika internet memblokir gambar, teks tetap terbaca.

## 4. Menambah/merevisi isi materi

Lihat `materi.json`: struktur `chapters -> sections -> lessons`. Setiap `lesson` memuat judul, submateri, penjelasan, analogi, rumus, contoh per langkah, pemeriksaan C2, dan miskonsepsi. Untuk menggunakan JSON hasil edit sebagai data situs, jalankan di komputer (Python 3):

```python
from pathlib import Path
p = Path('materi.json')
Path('materi.js').write_text('window.PA_MATERI = ' + p.read_text(encoding='utf-8') + ';\n', encoding='utf-8')
```

Setelah itu unggah ulang `materi.js` ke GitHub. **Jangan** jalankan `build_content.py` setelah mengedit `materi.json` jika ingin mempertahankan perubahan manual pada JSON karena script tersebut menimpa JSON.

## 5. Uji coba tanpa upload

Unduh folder hasil ekstrak. Jika seluruh 4 file inti berada satu folder, buka `index.html` langsung dengan Chrome. Situs tidak butuh server untuk memuat materi karena data berasal dari `materi.js`, bukan `fetch()` JSON. Koneksi internet hanya diperlukan untuk foto dari Unsplash.

Uji: buka setiap bab, pilih materi, jawab kuis, tandai selesai, segarkan halaman, uji pencarian dan layar ponsel.

## 6. Catatan pedagogis dan hak penggunaan

- Isi pembahasan **disusun ulang secara orisinal** untuk memudahkan pembaca awam; bukan salinan lengkap buku pemerintah.
- **Kurikulum inti kelas XII:** Barisan dan Deret, Investasi dan Pinjaman, Kaidah Pencacahan, Peluang. Distribusi kompetensi lain pada CP Fase F diatur melalui ATP sekolah.
- Rumus bunga/anuitas menggunakan asumsi tingkat bunga tetap dan waktu pembayaran teratur. Biaya kredit nyata dapat berbeda.
- Hasil probabilitas teoretis memakai asumsi yang ditulis, misalnya koin/dadu seimbang.
- Hak foto sesuai lisensi Unsplash; kredit dan tautan fotografer tersedia di bagian paling bawah situs. Foto diambil secara remote agar ukuran repository kecil.
- Tidak ada data siswa yang dikirim keluar. Tidak memakai Analytics, Supabase, autentikasi, atau penilaian guru.

**Sumber resmi:** https://buku.kemendikdasmen.go.id/katalog/matematika-untuk-smamasmkmak-kelas-xii-edisi-revisi

**CP Fase F:** https://repositori.kemendikdasmen.go.id/33608/
