import json, pathlib, re
ROOT=pathlib.Path(__file__).parent
C=[]

def chapter(title,overview,essential,project,project_steps,image,credit):
    C.append({'title':title,'overview':overview,'essential':essential,'project':project,'project_steps':project_steps,'image':image,'credit':credit,'sections':[]})

def section(title,goal,c4):
    C[-1]['sections'].append({'title':title,'goal':goal,'c4':c4,'lessons':[]})

def L(title,subtopics,explain,analogy,formula,problem,steps,answer,check,options,correct,feedback,trap):
    assert len(options)==3 and 0<=correct<=2
    C[-1]['sections'][-1]['lessons'].append({'title':title,'subtopics':subtopics.split(';'),'explain':explain,'analogy':analogy,'formula':formula,'example':{'problem':problem,'steps':steps.split(';'),'answer':answer},'check':{'question':check,'options':options,'correct':correct,'feedback':feedback},'trap':trap})

photos={
 'barisan':'https://images.unsplash.com/photo-1518336751805-17d4ea1ba5a0?auto=format&fit=crop&w=1400&q=82',
 'keuangan':'https://images.unsplash.com/photo-1707902665498-a202981fb5ac?auto=format&fit=crop&w=1400&q=82',
 'pencacahan':'https://images.unsplash.com/photo-1714403160710-9fd8e2206b33?auto=format&fit=crop&w=1400&q=82',
 'peluang':'https://images.unsplash.com/photo-1597591406871-b57baac13802?auto=format&fit=crop&w=1400&q=82'
}

chapter('Barisan dan Deret',
 'Pernah melihat kursi yang berbaris rapi, tabungan yang terus bertambah, atau benda yang jumlahnya berlipat? Semua dapat dijelaskan dengan pola bilangan.',
 'Membedakan barisan (daftar bilangan) dengan deret (jumlah bilangan), mengenali beda atau rasio, lalu memakai rumus hanya setelah memahami polanya.',
 'Proyek 1 · Rencana menabung untuk kegiatan kelas',
 ['Pilih target dana, misalnya Rp600.000 dalam 12 minggu.','Buat skenario setoran tetap dan setoran bertambah Rp2.000 setiap minggu.','Tulis tabel setoran dan total tabungan; cocokkan hasil dengan rumus deret.','Presentasikan pilihan yang paling realistis disertai alasan dan batasan.'],
 photos['barisan'],'Foto CHUTTERSNAP / Unsplash')
section('Pengenalan Pola Bilangan dan Barisan','Mengenali keteraturan sebelum memakai simbol atau rumus.','Dua barisan berawal dari 2, 4, 6. Barisan A meneruskan +2, barisan B meneruskan +2 lalu berubah menjadi ×2. Mengapa tiga suku saja belum cukup menentukan satu aturan secara pasti?')
L('Konsep dasar pola bilangan','pola naik, turun, dan berulang;selisih antarsuku;aturan pembentuk;representasi dengan benda',
 'Pola adalah susunan yang mengikuti aturan. Pola tidak selalu bertambah: bisa berkurang, berulang, atau berganti aturan. Saat melihat 3, 6, 9, 12, jangan langsung menghafal rumus. Pertama-tama bandingkan dua bilangan yang berdekatan. Setiap suku bertambah tiga.',
 'Bayangkan rak perpustakaan: rak pertama berisi 3 buku, rak kedua 6 buku, rak ketiga 9 buku. Kamu bisa memprediksi rak keempat tanpa menghitung dari awal.',
 'Jika selisih selalu sama, pola itu bersifat aritmetika.',
 'Lanjutkan pola 4, 7, 10, 13, ... sebanyak dua suku.',
 'Periksa 7 − 4 = 3, 10 − 7 = 3, dan 13 − 10 = 3;Aturannya adalah menambah 3 setiap langkah;Suku berikutnya 13 + 3 = 16, lalu 16 + 3 = 19.',
 '16 dan 19', 'Apa aturan paling sederhana untuk 8, 13, 18, 23, ...?', ['Tambah 5','Kali 5','Kurang 5'],0,'Setiap bilangan naik tepat 5.',
 'Satu deret angka kadang dapat dibuat dari banyak aturan. Selalu nyatakan aturan yang dipakai.')
L('Konsep barisan bilangan','pengertian suku;nomor urut;notasi Uₙ;menebak suku berikut',
 'Barisan adalah daftar bilangan yang ditulis menurut urutannya. Angka pertama disebut suku pertama (U₁); angka kedua suku kedua (U₂). Simbol Uₙ berarti nilai suku pada urutan ke-n. Huruf n bukan nilai suku, melainkan nomor posisinya.',
 'Seperti nomor kursi bioskop: kursi ke-5 berbeda dengan jumlah seluruh kursi. Nomor urut bukan nilai isi.',
 'U₁ = suku pertama; U₂ = suku kedua; Uₙ = suku ke-n.',
 'Pada barisan 5, 10, 15, 20, ..., berapa U₃ dan U₅?',
 'U₃ adalah bilangan di urutan ketiga, yaitu 15;Setiap suku naik 5;U₅ = 20 + 5 = 25.',
 'U₃ = 15 dan U₅ = 25', 'Apa arti U₄?', ['Jumlah empat suku','Nilai suku keempat','Empat kali suku pertama'],1,'U₄ menunjuk satu suku, yaitu yang menempati posisi keempat.',
 'Jangan tertukar antara nomor urut n dan nilai suku Uₙ.')
section('Barisan Aritmetika','Menemukan beda tetap dan menghitung suku tertentu.','Siswa A menabung Rp10.000 lalu menaikkan setoran Rp2.000 tiap minggu. Siswa B selalu menyetor Rp20.000. Bandingkan setoran pada minggu ke-8 dan jelaskan apakah jumlah tabungan mereka juga lebih besar pada minggu itu.')
L('Konsep barisan aritmetika','beda tetap b;suku pertama a;barisan naik atau turun;rumus suku ke-n',
 'Barisan aritmetika memiliki selisih yang sama antara dua suku berurutan. Selisih ini disebut beda (b). Suku pertama disebut a. Untuk mencari suku ke-n, kamu tidak perlu menulis semua suku: cukup dari a melangkah sebanyak n − 1 kali, masing-masing sebesar b.',
 'Naik tangga dengan tinggi anak tangga sama: dari anak tangga pertama ke kelima ada empat perpindahan, bukan lima.',
 'Uₙ = a + (n − 1)b; b = U₂ − U₁.',
 'Tentukan U₈ dari 7, 11, 15, 19, ...',
 'Suku pertama a = 7;Beda b = 11 − 7 = 4;U₈ = 7 + (8 − 1) × 4 = 7 + 28 = 35.',
 'U₈ = 35', 'Barisan 20, 16, 12, 8 memiliki beda ...', ['4','−4','−8'],1,'Beda = 16 − 20 = −4; tanda minus berarti menurun.',
 'Kesalahan umum: menghitung n kali beda, padahal dari suku pertama ada n−1 langkah.')
L('Penerapan barisan aritmetika','menentukan a dan b;menyisipkan suku;model biaya atau jumlah;menjelaskan satuan',
 'Masalah cerita akan lebih mudah jika kita menentukan tiga hal: suku pertama, beda setiap periode, dan nomor periode yang ditanyakan. Pastikan satuan waktu konsisten, misalnya semuanya dalam minggu.',
 'Pada barisan lampu jalan, lampu pertama berjarak 2 m dari titik awal lalu setiap lampu berikutnya berjarak 5 m dari lampu sebelumnya.',
 'Uₙ = a + (n − 1)b.',
 'Setoran minggu pertama Rp8.000 dan bertambah Rp3.000 tiap minggu. Berapa setoran minggu ke-6?',
 'a = Rp8.000; b = Rp3.000 tiap minggu; n = 6;U₆ = 8.000 + (6 − 1) × 3.000 = 23.000.',
 'Rp23.000', 'Jika suku pertama 9 dan beda 2, U₄ adalah ...', ['15','17','18'],0,'U₄ = 9 + (4−1)×2 = 15.',
 'Setoran pada minggu ke-6 berbeda dengan total seluruh setoran dari minggu pertama sampai keenam.')
section('Barisan Geometri','Menemukan rasio dan membedakan pertumbuhan tetap dari pelipatan.','Bandingkan barisan 5, 10, 15, 20 dan 5, 10, 20, 40. Mana yang paling cepat membesar dan mengapa?')
L('Konsep barisan geometri','rasio tetap r;pangkat sebagai pengulangan kali;rumus suku ke-n;geometri bertambah atau menyusut',
 'Berbeda dengan aritmetika yang menambah jumlah tetap, barisan geometri mengalikan setiap suku dengan angka yang sama. Angka pengali itu disebut rasio (r). Rasio 2 berarti setiap langkah menjadi dua kali, sedangkan rasio 1/2 berarti setiap langkah menjadi setengahnya.',
 'Bayangkan kertas yang dilipat menjadi dua: jumlah lapisan menjadi 1, 2, 4, 8, dan seterusnya.',
 'Uₙ = a × r^(n−1); r = U₂ ÷ U₁ (jika U₁ ≠ 0).',
 'Tentukan suku ke-5 dari 3, 6, 12, 24, ...',
 'a = 3; r = 6 ÷ 3 = 2;U₅ = 3 × 2^(5−1) = 3 × 16 = 48.',
 'U₅ = 48', 'Rasio barisan 81, 27, 9, 3 adalah ...', ['3','1/3','−3'],1,'27 ÷ 81 = 1/3, sehingga setiap suku menjadi sepertiga.',
 'Beda (pengurangan) dan rasio (pembagian) adalah dua hal berbeda.')
L('Penerapan barisan geometri','menentukan r;pelipatan berulang;penyusutan berulang;memeriksa kewajaran hasil',
 'Bila sebuah jumlah berubah dengan persentase yang sama setiap periode, bentuknya sering berupa barisan geometri. Kenaikan 10% berarti dikali 1,10; penyusutan 20% berarti dikali 0,80. Persentase tidak ditambahkan begitu saja ke jumlah awal pada setiap tahap.',
 'Sejumlah sel membelah menjadi dua dalam periode tetap sehingga banyak sel mengikuti 2, 4, 8, 16, ....',
 'Jumlah setelah n perubahan = jumlah awal × (faktor)^n.',
 'Sebuah populasi awal 100 dan tumbuh 20% per tahun. Berapa setelah dua tahun?',
 'Faktor pertumbuhan = 1 + 20/100 = 1,2;Tahun pertama 100 × 1,2 = 120;Tahun kedua 120 × 1,2 = 144.',
 '144', 'Jumlah 200 menyusut 10% setiap periode. Faktor pengalinya ...', ['0,10','0,90','1,10'],1,'Sisa setelah turun 10% adalah 90% = 0,90 dari nilai sebelumnya.',
 'Pertumbuhan 20% dua kali bukan 40% dari nilai awal, melainkan 44% karena periode kedua memakai dasar baru.')
section('Deret Aritmetika','Memahami jumlah beberapa suku yang berbeda tetap.','Seseorang menabung Rp5.000 pada minggu pertama, naik Rp2.000 tiap minggu selama 10 minggu. Apakah cukup menghitung setoran minggu ke-10 untuk mengetahui total tabungan? Jelaskan.')
L('Konsep deret aritmetika','deret versus barisan;jumlah Sₙ;pasangan suku;rumus jumlah',
 'Barisan menuliskan angka satu demi satu. Deret menjumlahkannya. Misalnya barisan 2, 4, 6, 8; deretnya 2 + 4 + 6 + 8 = 20. Untuk barisan aritmetika, jumlah bisa dihitung dengan memasangkan suku pertama dan terakhir.',
 'Seperti membayar iuran berbeda setiap minggu: untuk tahu jumlah uang terkumpul, seluruh iuran harus ditambahkan.',
 'Sₙ = n(a + Uₙ)/2 = n[2a + (n−1)b]/2.',
 'Hitung 3 + 7 + 11 + 15 + 19.',
 'Ada n = 5 suku;Suku pertama 3 dan suku terakhir 19;S₅ = 5 × (3 + 19) / 2 = 55.',
 '55', 'Apakah S₄ untuk barisan 2, 4, 6, 8?', ['8','16','20'],2,'S₄ adalah 2+4+6+8 = 20, bukan suku keempat.',
 'Uₙ adalah satu suku; Sₙ adalah total n suku pertama.')
L('Penerapan deret aritmetika','akumulasi tabungan;penjumlahan objek berpola;mencari banyak suku;menafsirkan hasil',
 'Saat soal berbunyi “jumlah seluruh”, “total”, atau “akumulasi”, besar kemungkinan kita perlu deret, bukan hanya suku terakhir. Tentukan banyak periode yang dihitung dan pastikan tidak ada periode terlewat.',
 'Menata kursi dengan 8 kursi pada baris pertama, 10 pada baris kedua, dan seterusnya: total kursi adalah jumlah seluruh baris.',
 'Sₙ = n[2a + (n−1)b]/2.',
 'Sebuah aula memiliki 4 baris kursi: 8, 10, 12, 14 kursi. Berapa semua kursi?',
 'a = 8, b = 2, n = 4;S₄ = 4 × [2(8)+3(2)]/2;S₄ = 2 × (16 + 6) = 44 kursi.',
 '44 kursi', 'Jumlah 5 + 8 + 11 + 14 adalah ...', ['38','30','14'],0,'5+8+11+14 = 38.',
 'Bila sedang menghitung total, jangan berhenti pada Uₙ.')
section('Deret Geometri','Menghitung total pertumbuhan yang berlipat, termasuk deret tak hingga yang konvergen.','Bola memantul setengah tinggi sebelumnya. Mengapa jumlah seluruh jarak pantulan bisa mendekati nilai tetap meskipun jumlah pantulannya sangat banyak?')
L('Deret geometri berhingga','jumlah suku dengan rasio;sifat rasio;rumus Sₙ;kasus r=1',
 'Deret geometri adalah penjumlahan suku-suku yang diperoleh dari pengalian rasio tetap. Misalnya 2 + 4 + 8 + 16 = 30. Rumusnya membantu saat banyak suku sangat besar. Jika r=1, semua suku sama sehingga cukup n×a.',
 'Bayangkan jumlah hadiah yang berlipat dua setiap tahap: tahap kedua 2 kali pertama, tahap ketiga 2 kali kedua.',
 'Sₙ = a(1−r^n)/(1−r) untuk r ≠ 1; jika r=1 maka Sₙ=na.',
 'Hitung total 3 + 6 + 12 + 24.',
 'a = 3, r = 2, n = 4;S₄ = 3(1−2⁴)/(1−2);S₄ = 3(−15)/(−1) = 45.',
 '45', 'Jumlah 2 + 6 + 18 adalah ...', ['26','24','18'],0,'Jumlah ketiga suku ialah 2+6+18 = 26.',
 'Saat r>1, bentuk 1−r^n dan 1−r sama-sama negatif; hasil jumlah tetap positif.')
L('Deret geometri tak hingga','makna mendekati batas;syarat |r|<1;rumus S∞;contoh pembagian berulang',
 'Tak hingga artinya proses penjumlahan dapat berlanjut tanpa batas. Namun, jika setiap suku makin kecil cukup cepat, totalnya justru mendekati bilangan tetap. Kondisi ini terjadi untuk deret geometri dengan −1 < r < 1.',
 'Potong sepotong pita: ambil setengah, lalu seperempat, lalu seperdelapan. Jumlah panjang yang diambil makin dekat ke satu pita utuh.',
 'S∞ = a/(1−r), hanya jika |r| < 1.',
 'Tentukan 8 + 4 + 2 + 1 + 1/2 + ...',
 'a = 8 dan r = 4 ÷ 8 = 1/2;Karena |r| = 1/2 < 1, deret memiliki jumlah terbatas;S∞ = 8/(1−1/2) = 16.',
 '16', 'Deret 5 + 10 + 20 + ... memiliki jumlah tak hingga yang terbatas?', ['Ya, karena sukunya bertambah','Tidak, karena |r| = 2','Ya, karena suku awalnya 5'],1,'Rasio 2 tidak memenuhi |r|<1 sehingga jumlahnya membesar tanpa batas.',
 'Simbol tak hingga bukan angka yang bisa langsung dimasukkan sebagai n dalam rumus biasa.')
section('Bunga Tunggal sebagai Penerapan','Menghubungkan perubahan tetap dengan keuangan dasar.','Apakah bunga tunggal 2% per bulan selama 6 bulan sama hasilnya dengan bunga majemuk 2% per bulan? Jelaskan penyebab perbedaan.')
L('Dasar matematika bunga tunggal','modal awal;tingkat bunga per periode;lama waktu;bunga tetap per periode',
 'Bunga tunggal dihitung selalu dari modal atau pokok awal yang sama. Karena dasar perhitungannya tidak berubah, nilai bunga per periode juga tetap. Ini mirip barisan aritmetika: saldo bertambah dengan beda yang sama.',
 'Meminjam Rp100.000 dengan bunga tunggal 1% per bulan berarti bunga per bulan Rp1.000 dari pokok awal, bukan dari saldo bulan sebelumnya.',
 'Bunga I = P × i × n; nilai akhir A = P + I = P(1+in).',
 'Modal Rp500.000 mendapat bunga tunggal 2% per bulan selama 3 bulan. Berapa bunga total?',
 'P = 500.000, i = 2/100 = 0,02, n = 3;Bunga per bulan = 500.000 × 0,02 = 10.000;Total bunga = 10.000 × 3 = Rp30.000.',
 'Rp30.000', 'Bunga tunggal dihitung dari ...', ['Saldo terus berubah','Modal awal','Jumlah seluruh bunga masa depan'],1,'Pada bunga tunggal, dasar penghitungan adalah pokok awal.',
 'Pastikan bunga per bulan dipasangkan dengan waktu dalam bulan; bunga per tahun dengan waktu dalam tahun.')
L('Penyelesaian masalah bunga tunggal','nilai akhir;menentukan lama waktu;menentukan tingkat bunga;perbandingan kasus',
 'Soal bunga tunggal sering menanyakan salah satu dari empat informasi: modal, tingkat bunga, waktu, atau nilai akhir. Tulis yang diketahui dahulu lalu pindahkan unsur persamaan secara bertahap.',
 'Jika uang di tabungan bertambah Rp10.000 setiap bulan, totalnya naik teratur walaupun lamanya terus bertambah.',
 'A = P(1+in), dengan i ditulis sebagai desimal.',
 'Uang Rp400.000 berbunga tunggal 1% per bulan selama 5 bulan. Tentukan saldo akhirnya.',
 'i = 0,01 dan n = 5;Bunga total = 400.000 × 0,01 × 5 = 20.000;Saldo akhir = 400.000 + 20.000 = Rp420.000.',
 'Rp420.000', 'Saldo akhir dari modal Rp100.000 dengan bunga tunggal 10% untuk satu periode?', ['Rp110.000','Rp101.000','Rp200.000'],0,'10% × 100.000 = 10.000, jadi total 110.000.',
 'Nilai akhir adalah modal ditambah bunga; bukan hanya besarnya bunga.')

chapter('Investasi dan Pinjaman',
 'Mengapa dua tawaran tabungan dengan persentase bunga sama bisa memberikan hasil berbeda? Mengapa cicilan tetap tetap memiliki bagian bunga dan pokok yang berubah?',
 'Mengenali uang awal, persentase per periode, waktu, dan arus kas. Seluruh contoh merupakan simulasi pembelajaran, bukan ajakan membeli produk keuangan.',
 'Proyek 2 · Membandingkan tabungan dan biaya cicilan',
 ['Gunakan data hipotetis: tabungan awal Rp1.000.000, tingkat bunga 1% per bulan selama 12 bulan.','Bandingkan bunga tunggal dan majemuk serta hitung selisihnya.','Buat satu skenario cicilan anuitas dengan tabel saldo, bunga, dan pelunasan pokok.','Tulis keputusan berdasarkan total biaya/manfaat dan sebutkan asumsi model.'],
 photos['keuangan'],'Foto Jakub Żerdzicki / Unsplash')
section('Konsep Suku Bunga Tunggal','Memahami bahasa keuangan paling dasar sebagai prasyarat.','Bank A menawarkan bunga tunggal 12% per tahun, bank B 1% per bulan. Apakah kedua bunga setara jika tidak ada pemajemukan? Jelaskan satuan waktunya.')
L('Dasar suku bunga','arti persentase;tingkat bunga dan periode;pokok P;perbedaan bunga dan saldo',
 'Persentase berarti “per seratus”. Bunga 5% berarti setiap Rp100 dari pokok menghasilkan Rp5 bunga untuk periode yang disebutkan. Periode sangat penting: 5% per bulan tidak sama dengan 5% per tahun.',
 'Label harga diskon 10% memberi gambaran bahwa persentase perlu dikalikan dengan angka acuan.',
 '5% = 5/100 = 0,05; I = P × i × n untuk bunga tunggal.',
 'Hitung bunga satu tahun dari Rp2.000.000 dengan bunga tunggal 6% per tahun.',
 'Ubah 6% menjadi 0,06;Kalikan pokok × bunga: 2.000.000 × 0,06;Hasil bunga satu tahun Rp120.000.',
 'Rp120.000', 'Suku bunga 3% dalam desimal adalah ...', ['0,3','0,03','3'],1,'3 dibagi 100 sama dengan 0,03.',
 'Jangan lupa membagi persentase dengan 100 sebelum mengalikannya.')
L('Analisis bunga tunggal','mencari I;mencari A;mencari i atau n;menyelaraskan satuan',
 'Semua persoalan bunga tunggal dapat dimulai dari rumus I=P×i×n. Jika yang tidak diketahui tingkat bunganya, bagi kedua sisi dengan P×n. Jika tidak diketahui waktunya, bagi dengan P×i.',
 'Seperti resep makanan: jika tahu jumlah porsi dan bahan total, kamu dapat mencari bahan per porsi.',
 'i = I/(P×n); n = I/(P×i), bila pembagi bukan nol.',
 'Bunga Rp60.000 diperoleh dari modal Rp500.000 selama 2 tahun. Berapa suku bunga tunggal per tahun?',
 'I=60.000, P=500.000, n=2 tahun;i = 60.000/(500.000×2)=0,06;Suku bunga per tahun = 6%.',
 '6% per tahun', 'Bunga Rp20.000 dari modal Rp100.000 selama 2 tahun berarti bunga per tahun ...', ['10%','20%','5%'],0,'20.000/(100.000×2)=0,10=10% per tahun.',
 'Suku bunga tanpa satuan waktu belum cukup untuk dipakai menghitung.')
section('Investasi dengan Bunga Majemuk','Mengenali bunga berbunga dan pengaruh periode.','Apakah dua kali pertumbuhan 10% sama dengan sekali pertumbuhan 20%? Uji menggunakan modal Rp100.000.')
L('Konsep bunga majemuk','bunga berbunga;faktor 1+i;perbedaan dengan bunga tunggal;rumus A',
 'Pada bunga majemuk, bunga periode pertama ditambahkan ke saldo. Periode berikutnya, bunga dihitung dari saldo baru tersebut. Karena itu, saldo sering tumbuh seperti barisan geometri.',
 'Tanaman yang setiap bulan tumbuh 10% dari ukurannya sekarang akan tumbuh makin besar dalam ukuran absolut.',
 'A = P(1+i)^n, jika bunga diterapkan sekali tiap periode.',
 'Hitung nilai akhir Rp1.000.000 dengan bunga majemuk 10% per tahun selama 2 tahun.',
 'Tahun pertama: 1.000.000×1,10 = 1.100.000;Tahun kedua: 1.100.000×1,10 = 1.210.000;Rumus cepat: 1.000.000×(1,10)^2 = 1.210.000.',
 'Rp1.210.000', 'Bunga periode kedua pada bunga majemuk dihitung dari ...', ['Pokok awal saja','Saldo awal periode kedua','Suku bunga tahun pertama saja'],1,'Bunga majemuk selalu menghitung dari saldo yang sudah mencakup bunga sebelumnya.',
 'Pada model sederhana ini belum diperhitungkan pajak, biaya administrasi, dan perubahan suku bunga.')
L('Analisis hasil investasi','menghitung hasil bersih bunga;membandingkan skenario;periode pemajemukan;memeriksa hasil',
 'Untuk membandingkan investasi, samakan nilai awal, satuan tingkat bunga, dan lamanya. Bunga majemuk dengan bunga nominal tahunan yang sama dapat menghasilkan hasil berbeda jika frekuensi pemajemukannya berbeda.',
 'Dua tabungan seperti dua tanaman yang disiram dengan jadwal berbeda; waktunya memengaruhi proses pertumbuhan.',
 'A = P(1+j/m)^(mt) untuk bunga nominal j per tahun, m kali pemajemukan setahun, selama t tahun.',
 'Modal Rp1.000.000 mendapat 12% nominal per tahun dengan bunga dibukukan tiap bulan. Berapa nilai akhir setelah 2 bulan?',
 'Bunga tiap bulan = 12%/12 = 1% = 0,01;Jumlah periode n=2 bulan;A=1.000.000×(1,01)^2=Rp1.020.100.',
 'Rp1.020.100', 'Bila bunga majemuk 1% per bulan selama 2 bulan, faktor pengalinya ...', ['1,01²','1,02','0,99²'],0,'Setiap bulan dikali 1,01, maka dua bulan dikali 1,01².',
 'Perhatikan perbedaan tingkat bunga efektif dan nominal; jangan memakai 12% sebagai bunga tiap bulan.')
section('Investasi dengan Anuitas','Memahami setoran sama besar yang dilakukan berulang.','Jika menyetor uang setiap awal bulan dan setiap akhir bulan, mana yang berpotensi menghasilkan nilai akhir lebih besar dengan bunga positif?')
L('Dasar anuitas investasi','setoran berkala R;akhir vs awal periode;nilai akhir;jumlah setoran',
 'Anuitas berarti pembayaran atau setoran dengan jumlah tetap pada setiap periode. Pada anuitas biasa, setoran masuk di akhir periode. Setoran awal periode mendapat tambahan satu periode bunga lebih lama, sehingga hasilnya sedikit lebih tinggi jika bunganya positif.',
 'Menaruh satu koin di celengan setiap akhir pekan berbeda dari membayar semua koin sekaligus di awal; uang yang lebih dulu disimpan bekerja lebih lama.',
 'FV anuitas biasa = R[((1+i)^n−1)/i] untuk i ≠ 0; untuk i=0, FV=nR.',
 'Menabung Rp100.000 di akhir setiap tahun selama 2 tahun dengan bunga 10% per tahun. Berapa nilai akhirnya tepat setelah setoran kedua?',
 'Setoran tahun pertama berkembang 1 tahun menjadi 100.000×1,10=110.000;Setoran tahun kedua baru masuk Rp100.000;Jumlah nilai akhir = Rp210.000.',
 'Rp210.000', 'Dalam anuitas biasa, setoran dilakukan pada ...', ['Awal periode','Akhir periode','Waktu acak'],1,'Anuitas biasa menggunakan setoran akhir setiap periode.',
 'Selalu jelaskan setoran dilakukan awal atau akhir periode; hasilnya berbeda.')
L('Perencanaan investasi berkala','target dana;menentukan setoran;simulasi tabel;nilai kini dan nilai masa depan',
 'Jika target tabungan diketahui, rumus anuitas bisa dibalik untuk mengetahui setoran tetap yang diperlukan. Dalam praktik belajar, tabel per periode sering lebih mudah dipahami daripada rumus yang panjang.',
 'Membagi target biaya wisata menjadi beberapa setoran tetap membuat rencana lebih terukur.',
 'R = FV×i / [(1+i)^n−1] untuk anuitas biasa dan i ≠ 0.',
 'Target Rp300.000 setelah 3 bulan tanpa bunga. Berapa setoran tiap akhir bulan?',
 'Nilai target = 300.000 dan n=3;Karena tidak ada bunga, cukup membagi 300.000 dengan 3;Setoran setiap bulan = Rp100.000.',
 'Rp100.000 per bulan', 'Untuk target Rp600.000 dalam 6 bulan tanpa bunga, setoran tetap per bulan ...', ['Rp60.000','Rp100.000','Rp120.000'],1,'600.000 ÷ 6 = Rp100.000.',
 'Jangan menyamakan jumlah semua setoran dengan nilai akhir saat ada bunga; ada tambahan hasil bunga.')
section('Pinjaman dengan Bunga Majemuk','Menjelaskan utang yang belum dilunasi dapat berkembang.','Mengapa menunda pembayaran utang berbunga majemuk dapat meningkatkan jumlah yang harus dibayar meskipun pokok awal tidak berubah?')
L('Konsep pinjaman','pokok pinjaman;saldo kewajiban;tingkat bunga;pertumbuhan bila tanpa angsuran',
 'Pinjaman adalah uang yang diterima sekarang dan harus dikembalikan kemudian. Pada model bunga majemuk tanpa pembayaran selama periode tertentu, utang meningkat karena bunga masuk ke saldo kewajiban.',
 'Meminjam alat lalu dikenakan tambahan biaya setiap waktu menggambarkan mengapa durasi memengaruhi total yang ditanggung.',
 'Saldo tanpa pembayaran A=P(1+i)^n.',
 'Pinjaman Rp500.000 memiliki bunga majemuk 10% per tahun dan belum dibayar 2 tahun. Berapa saldo teoretisnya?',
 'Tahun pertama 500.000×1,1=550.000;Tahun kedua 550.000×1,1=605.000;Saldo kewajiban = Rp605.000.',
 'Rp605.000', 'Jika pokok utang Rp100.000 tumbuh 10% setahun tanpa pembayaran, saldo setahun kemudian ...', ['Rp90.000','Rp110.000','Rp100.000'],1,'10% dari 100.000 adalah 10.000 sehingga totalnya 110.000.',
 'Model sederhana ini belum memasukkan denda, biaya lain, atau peraturan kredit tertentu.')
L('Analisis biaya pinjaman','saldo setelah n periode;bandingkan suku bunga;dampak waktu;biaya total',
 'Biaya pinjaman bukan hanya angka cicilan bulanan. Untuk membandingkan, perhatikan jumlah pembayaran keseluruhan dan tambahan biaya yang mungkin dikenakan. Semakin lama utang dibiarkan bertumbuh, umumnya semakin tinggi kewajiban pada model majemuk.',
 'Harga barang dengan pembayaran cicilan harus dibandingkan dengan harga tunai menggunakan total biaya.',
 'Biaya bunga teoretis = saldo akhir − pokok awal, untuk pinjaman tanpa pembayaran.',
 'Pinjaman Rp1.000.000 berbunga majemuk 5% per tahun selama 2 tahun tanpa pembayaran. Berapa bunga total?',
 'Saldo akhir = 1.000.000×1,05² = 1.102.500;Kurangi pokok awal 1.000.000;Bunga total = Rp102.500.',
 'Rp102.500', 'Jika saldo akhir Rp1.210.000 dan pokok Rp1.000.000, selisih biaya bunga adalah ...', ['Rp210.000','Rp121.000','Rp21.000'],0,'1.210.000 − 1.000.000 = 210.000.',
 'Jangan membandingkan dua pinjaman hanya dari cicilan terendah: cek lama waktu dan total biaya.')
section('Pinjaman dengan Anuitas','Membedakan angsuran, bunga, dan pelunasan pokok.','Mengapa pada angsuran total yang tetap, bagian bunga cenderung turun dari bulan ke bulan?')
L('Sistem angsuran anuitas','angsuran tetap R;bunga periodik;angsuran pokok;sisa utang',
 'Dalam sistem anuitas dengan tingkat bunga tetap, total pembayaran per periode sama. Namun isinya berubah: ketika utang masih besar, bunga juga besar; setelah utang berkurang, bagian bunga mengecil dan bagian pelunasan pokok membesar.',
 'Membayar biaya sewa alat dan mencicil harga alat dalam satu tagihan: sebagian tagihan adalah biaya, sebagian mengurangi utang.',
 'R = Pi / [1−(1+i)^(−n)] untuk i ≠ 0; bunga periode = saldo awal × i.',
 'Saldo utang Rp1.000.000 dengan bunga 1% per bulan; angsuran bulanan tetap Rp350.000. Berapa pokok yang terbayar bulan pertama?',
 'Bunga bulan pertama = 1%×1.000.000 = 10.000;Dari angsuran Rp350.000, Rp10.000 digunakan membayar bunga;Pelunasan pokok = 350.000−10.000 = Rp340.000.',
 'Rp340.000 pokok terbayar', 'Jika angsuran Rp500.000 terdiri dari bunga Rp75.000, pengurangan pokok adalah ...', ['Rp575.000','Rp425.000','Rp75.000'],1,'Angsuran pokok = 500.000−75.000 = 425.000.',
 'Contoh angsuran Rp350.000 di atas hanya ilustrasi pemecahan komponen, bukan klaim cicilan lunas sesuai rumus untuk tenor tertentu.')
L('Tabel amortisasi','saldo awal;bunga angsuran;pengurangan pokok;saldo akhir;pelunasan',
 'Tabel amortisasi menunjukkan perjalanan utang dari periode ke periode. Empat kolom utama adalah saldo awal, bunga, pokok yang dilunasi, dan saldo akhir. Saldo akhir satu periode menjadi saldo awal periode berikutnya.',
 'Seperti buku kas kelas: setiap pembayaran dicatat agar sisa kewajiban diketahui.',
 'Pokok terbayar = angsuran−bunga; saldo akhir = saldo awal−pokok terbayar.',
 'Saldo awal Rp600.000, bunga bulan ini 2%, dan dibayar Rp212.000. Tentukan saldo akhir.',
 'Bunga = 600.000×0,02 = 12.000;Pokok yang terbayar = 212.000−12.000 = 200.000;Saldo akhir = 600.000−200.000 = Rp400.000.',
 'Rp400.000', 'Sisa utang awal Rp500.000, pokok yang terbayar Rp120.000, saldo akhir ...', ['Rp380.000','Rp620.000','Rp500.000'],0,'Kurangi 500.000 dengan 120.000.',
 'Selalu periksa: saldo akhir tidak boleh bertambah jika bunga sudah tercakup dan pembayaran lebih besar daripada bunga.')
section('Pengaruh Parameter Investasi dan Pinjaman','Menguji apa yang terjadi ketika suatu asumsi diubah.','Dua kredit memiliki cicilan bulanan berbeda. Mengapa cicilan bulanan yang lebih rendah belum tentu lebih murah secara total?')
L('Analisis perubahan parameter','parameter bunga;parameter periode;frekuensi setoran;perbandingan grafik',
 'Parameter adalah angka yang bisa diubah dalam model, misalnya tingkat bunga dan lama waktu. Untuk mempelajari pengaruh suatu parameter, ubah satu hal saja sementara hal lain dibuat sama. Cara ini mencegah kesimpulan yang keliru.',
 'Dalam eksperimen memasak, jika rasa berubah saat gula dan garam sama-sama diganti, sulit mengetahui penyebabnya.',
 'Pada bunga majemuk A=P(1+i)^n, i dan n memengaruhi A.',
 'Modal Rp1.000.000 selama 1 tahun. Bandingkan bunga majemuk 5% dan 10%, masing-masing dibukukan setahun sekali.',
 'Jika 5%, A=1.000.000×1,05=Rp1.050.000;Jika 10%, A=1.000.000×1,10=Rp1.100.000;Selisih Rp50.000, dengan asumsi lain sama.',
 'Selisih Rp50.000', 'Untuk membandingkan dampak bunga secara adil, apa yang harus dijaga sama?', ['Modal awal dan durasi','Warna grafik','Nama bank'],0,'Modal dan durasi harus sama agar yang berubah hanya tingkat bunga.',
 'Hasil model tidak sama dengan kepastian hasil produk keuangan nyata.')
L('Pengambilan keputusan finansial','bunga dan biaya tambahan;total cicilan;inflasi dasar;asumsi dan risiko',
 'Keputusan finansial memerlukan pertanyaan lebih luas daripada “berapa bunganya”. Perhatikan biaya layanan, lama kontrak, kemampuan membayar, kemungkinan perubahan tingkat bunga, dan nilai uang dari waktu ke waktu. Model matematika membantu, tetapi tidak menggantikan penilaian risiko.',
 'Dua toko menawarkan cicilan: yang satu cicilannya kecil tapi lebih lama, sehingga jumlah akhirnya bisa lebih besar.',
 'Total pembayaran = jumlah seluruh cicilan + biaya lain yang tidak termasuk cicilan.',
 'Pilihan A: 10 cicilan Rp120.000. Pilihan B: 12 cicilan Rp105.000. Tanpa biaya lain, mana lebih kecil?',
 'Total A = 10×120.000 = 1.200.000;Total B = 12×105.000 = 1.260.000;A lebih murah Rp60.000 meskipun cicilan per bulannya lebih besar.',
 'Pilihan A, selisih Rp60.000', 'Yang harus dibandingkan saat menilai biaya kredit adalah ...', ['Cicilan per bulan saja','Total pembayaran dan persyaratan','Warna brosur'],1,'Lihat biaya total beserta syarat pembayarannya.',
 'Materi ini untuk literasi matematika, bukan rekomendasi transaksi atau pinjaman tertentu.')

chapter('Kaidah Pencacahan',
 'Berapa banyak cara memilih pakaian, menyusun kode, mengatur kursi, atau membentuk kepanitiaan? Kita dapat menghitungnya tanpa menuliskan satu per satu.',
 'Mulailah dengan bertanya: apakah kita memilih salah satu cara, melakukan beberapa tahap, menyusun urutan, atau hanya memilih anggota?',
 'Proyek 3 · Sistem pengaturan panitia dan jadwal',
 ['Data beberapa jabatan panitia dan calon pengurus (tanpa data pribadi sensitif).','Tentukan jumlah cara ketika jabatan berbeda dan ketika hanya memilih anggota.','Buat tabel atau skrip sederhana untuk menampilkan beberapa kemungkinan.','Jelaskan kapan menggunakan permutasi dan kapan kombinasi.'],
 photos['pencacahan'],'Foto One Pixel / Unsplash')
section('Aturan Pengisian Tempat','Menghitung cara tanpa harus mendaftar satu per satu.','Kantin menawarkan dua jenis nasi atau tiga jenis mi untuk satu menu. Sementara itu, satu paket harus memilih satu nasi dan satu minuman. Mengapa cara hitungnya berbeda?')
L('Aturan penjumlahan','pilihan alternatif;kelompok saling terpisah;diagram kemungkinan;contoh transportasi',
 'Aturan penjumlahan dipakai ketika kita memilih salah satu dari beberapa kelompok pilihan yang tidak tumpang tindih. Kata kuncinya adalah “atau”. Jika tersedia 3 jenis jus atau 2 jenis teh dan kita memilih satu minuman, ada 5 pilihan.',
 'Di perpustakaan ada 4 novel atau 3 komik untuk dipinjam satu saja; jumlah pilihan 7.',
 'Banyak pilihan total = pilihan A + pilihan B, bila keduanya tidak beririsan.',
 'Ada 4 rute bus atau 3 rute kereta, dan seseorang hanya memilih salah satu rute. Berapa alternatif?',
 'Ada 4 pilihan bus;Ada 3 pilihan kereta dan kelompoknya berbeda;Jumlah alternatif = 4 + 3 = 7.',
 '7 alternatif', 'Pilih satu: 5 jenis kue atau 2 jenis buah. Banyak pilihan ...', ['7','10','3'],0,'Kata “atau” menunjukkan pilihan alternatif: 5+2=7.',
 'Jika suatu pilihan masuk dua kategori sekaligus, perlu menghindari penghitungan ganda.')
L('Aturan perkalian','pilihan berurutan;diagram pohon;pasangan;slot pilihan',
 'Aturan perkalian digunakan jika satu keputusan terdiri atas beberapa tahap yang semuanya dilakukan. Kata kuncinya adalah “dan”. Jika 3 baju bisa dipasangkan dengan 2 celana, setiap baju memiliki 2 pasangan sehingga total 6.',
 'Memilih baju DAN celana: yang dihitung bukan jenis baju saja, melainkan seluruh pasangan.',
 'Total cara = cara tahap 1 × cara tahap 2 × ... .',
 'Ada 3 pilihan roti dan 2 pilihan minuman. Berapa paket berbeda jika setiap paket berisi keduanya?',
 'Setiap roti dapat dipasangkan dengan 2 minuman;Ada 3 jenis roti;Total 3×2 = 6 paket.',
 '6 paket', 'Jika 4 topi bisa dipasangkan dengan 3 kaus, jumlah pasangan ...', ['7','12','1'],1,'Setiap topi punya tiga pasangan, jadi 4×3=12.',
 'Gunakan perkalian hanya jika semua tahapan dilakukan, bukan hanya memilih salah satu.')
section('Faktorial dan Permutasi','Memahami jumlah susunan ketika posisi penting.','Ada 3 kandidat untuk jabatan ketua, sekretaris, dan bendahara. Apakah memilih kelompok 3 orang sama dengan menentukan tiga jabatan itu?')
L('Konsep faktorial','arti n!;0!;urutan perkalian;penyederhanaan',
 'Faktorial adalah perkalian bilangan bulat positif berurutan sampai 1. Misalnya 4! = 4×3×2×1 = 24. Faktorial sering dipakai karena jumlah pilihan berkurang setelah satu posisi terisi. Secara definisi 0! = 1.',
 'Menyusun tiga buku berbeda: buku pertama punya 3 pilihan, berikutnya tinggal 2, terakhir 1.',
 'n! = n×(n−1)×...×2×1; 0! = 1.',
 'Hitung 5!/3!.',
 'Tuliskan 5!=5×4×3!;Coret faktor 3! di atas dan di bawah;Hasil = 5×4 = 20.',
 '20', 'Nilai 4! adalah ...', ['16','24','12'],1,'4×3×2×1 = 24.',
 'Tanda ! dalam matematika ini bukan tanda seru biasa; ia memiliki arti faktorial.')
L('Permutasi unsur berbeda','arti urutan;memilih r dari n;rumus nPr;contoh jabatan',
 'Permutasi menghitung susunan ketika urutan atau jabatan membuat hasil berbeda. Pasangan (Ani, Budi) sebagai ketua-sekretaris berbeda dari (Budi, Ani). Jika mengambil r orang dari n calon, pilihan posisi pertama lebih banyak daripada posisi berikutnya.',
 'Juara 1 dan juara 2 tidak dapat saling ditukar tanpa mengubah hasil lomba.',
 'nPr = n!/(n−r)! untuk 0≤r≤n.',
 'Dari 4 calon, berapa susunan berbeda untuk ketua dan wakil?',
 'Ketua dapat dipilih dengan 4 cara;Sesudah ketua dipilih, wakil tersisa 3 cara;Total = 4×3 = 12 = 4P2.',
 '12 susunan', 'Pilih ketua dan sekretaris dari 3 orang, banyak susunan ...', ['3','6','9'],1,'3 pilihan ketua × 2 pilihan sekretaris = 6.',
 'Jika jabatan berbeda, urutan orang penting. Jangan memakai kombinasi.')
section('Permutasi dengan Unsur yang Sama','Menghindari susunan yang sebetulnya identik.','Mengapa 4 huruf pada kata MAMA tidak memiliki 4! susunan berbeda?')
L('Prinsip pengulangan unsur identik','objek identik;perhitungan ganda;faktor pembagi;rumus permutasi unsur sama',
 'Jika ada beberapa benda sama persis, menukarnya tidak menghasilkan susunan baru. Karena itu hasil n! harus dibagi dengan faktorial banyaknya benda yang sama pada setiap kelompok.',
 'Dua kaus putih yang benar-benar identik ditukar posisi tidak menciptakan susunan tampilan yang baru.',
 'Jumlah susunan = n!/(a!b!c!...) untuk kelompok unsur identik.',
 'Berapa susunan berbeda huruf AAB?',
 'Tanpa huruf sama: 3! = 6;Huruf A muncul 2 kali, sehingga dibagi 2!;Jumlah = 6/2 = 3: AAB, ABA, BAA.',
 '3 susunan', 'Susunan berbeda huruf AA ada ...', ['1','2','4'],0,'Menukar dua A tidak menimbulkan susunan baru.',
 'Penghitungan harus memperhatikan kelompok huruf/benda identik satu per satu.')
L('Penerapan permutasi unsur sama','susunan huruf;warna sama;syarat tambahan;cek daftar',
 'Untuk soal berbentuk kata, catat dulu banyak huruf dan berapa kali setiap huruf muncul. Setelah itu gunakan rumus dan, bila jumlah kecil, buat daftar susunan untuk memeriksa hasil.',
 'Menyusun kelereng dengan warna merah, merah, biru menghasilkan tiga tampilan: MMB, MBM, BMM.',
 'n!/(a!b!...), dengan n jumlah seluruh unsur.',
 'Berapa susunan berbeda huruf pada kata MAMA?',
 'Ada 4 huruf: M dua kali dan A dua kali;Jumlah = 4!/(2!×2!);Hasil 24/(2×2) = 6 susunan.',
 '6 susunan', 'Susunan dari BBBB adalah ...', ['1','4','24'],0,'Semua unsur sama sehingga hanya ada satu susunan unik.',
 'Tanda faktor pembagi untuk MAMA adalah 2!×2!, bukan 2+2.')
section('Permutasi Siklis','Menghitung susunan pada lingkaran secara tepat.','Empat orang duduk melingkar. Mengapa memutar seluruh kursi bersama-sama tidak dianggap susunan baru dalam model dasar?')
L('Konsep susunan melingkar','susunan melingkar;rotasi setara;mematok satu posisi;rumus siklis',
 'Di meja bundar, susunan yang hanya diputar bersama memiliki urutan tetangga sama. Untuk menghindari penghitungan berulang, tetapkan satu orang sebagai patokan lalu atur orang lainnya. Jika ada n orang berbeda, hasilnya (n−1)!.',
 'Bayangkan gelang huruf: memutar gelang tidak mengubah siapa bertetangga dengan siapa.',
 'Permutasi siklis = (n−1)! untuk n objek berbeda, bila putaran dianggap sama.',
 'Berapa cara menempatkan 4 orang berbeda di meja bundar?',
 'Tetapkan satu orang untuk menghilangkan rotasi ganda;Sisa 3 orang dapat disusun 3! cara;Hasil 3×2×1 = 6.',
 '6 cara', 'Tiga orang duduk melingkar memiliki susunan dasar sebanyak ...', ['2','3','6'],0,'(3−1)! = 2! = 2.',
 'Asumsi putaran setara berbeda dengan kasus kursi bernomor tetap; jelaskan konteksnya.')
L('Permutasi siklis berkondisi','harus berdampingan;tidak berdampingan;metode blok;memeriksa syarat',
 'Jika dua orang harus berdampingan, anggap keduanya satu blok terlebih dahulu. Atur blok itu bersama orang lain di lingkaran. Terakhir hitung berapa cara menukar posisi dua orang di dalam blok.',
 'Dua teman yang selalu duduk berdampingan dipandang sebagai satu pasangan saat mengatur kelompok.',
 'Untuk n orang melingkar, dua orang tertentu berdampingan: 2×(n−2)! (n≥3).',
 'Empat orang A, B, C, D duduk melingkar, A dan B harus berdampingan. Berapa susunan?',
 'Gabungkan A-B sebagai satu blok;Ada 3 objek melingkar: blok, C, dan D → (3−1)! = 2;A-B dapat ditukar menjadi B-A: ×2 sehingga total 4.',
 '4 susunan', 'Jika dua orang tertentu wajib berdampingan, langkah pertama yang mudah adalah ...', ['Menggabungkan menjadi satu blok','Menghapus satu orang','Menggunakan kombinasi tanpa urutan'],0,'Blok membantu memenuhi syarat kedekatan secara sistematis.',
 'Untuk syarat “tidak berdampingan”, sering lebih mudah: semua susunan − susunan berdampingan.')
section('Kombinasi','Mengenali masalah pemilihan yang tidak memperhatikan urutan.','Tim A berisi Ani, Budi, Cici. Apakah tim ini menjadi tim berbeda jika nama anggota ditulis Cici, Ani, Budi?')
L('Konsep kombinasi','memilih anggota;urutan tidak penting;rumus nCr;beda kombinasi-permutasi',
 'Kombinasi digunakan saat hanya isi kelompok yang penting. Memilih Ani dan Budi sama dengan memilih Budi dan Ani. Untuk menghapus susunan ulang yang sebenarnya sama, permutasi dibagi dengan r!.',
 'Isi keranjang dua apel yang sama tidak berubah hanya karena urutan mengambilnya ditukar.',
 'nCr = n!/[r!(n−r)!], untuk 0≤r≤n.',
 'Dari 4 siswa pilih 2 sebagai peserta lomba tanpa jabatan. Berapa kelompok?',
 'Hitung 4C2 = 4!/(2!×2!);Sederhanakan = (4×3)/(2×1);Hasil = 6 kelompok.',
 '6 kelompok', 'Memilih 2 anggota dari 3 siswa tanpa jabatan menghasilkan ...', ['3 kelompok','6 kelompok','9 kelompok'],0,'3C2 = 3, yaitu AB, AC, dan BC.',
 'Jangan memakai permutasi ketika urutan nama tidak mengubah kelompok.')
L('Penerapan kombinasi','pemilihan tim;panitia berkriteria;gabungan kelompok;syarat pilihan',
 'Soal kombinasi dapat mencakup syarat, misalnya harus memilih dua anggota dari kelompok A dan satu anggota dari B. Pisahkan dulu pilihan setiap kelompok, hitung kombinasi masing-masing, lalu kalikan karena semua syarat harus dipenuhi.',
 'Memilih 2 siswa kelas A dan 1 siswa kelas B berbeda dari mengurutkan ketiganya di panggung.',
 'Jika syarat bersamaan: total = C(n₁,r₁)×C(n₂,r₂).',
 'Pilih 2 siswa dari 4 laki-laki dan 1 siswa dari 3 perempuan. Berapa kelompok?',
 'Pilih 2 dari 4: 4C2=6;Pilih 1 dari 3: 3C1=3;Kedua pilihan harus dilakukan: 6×3 = 18.',
 '18 kelompok', 'Pilih 1 siswa dari 5 orang: 5C1 = ...', ['1','5','120'],1,'Ada lima calon yang masing-masing dapat menjadi satu anggota terpilih.',
 'Perhatikan kata “dan” antar-kriteria: jumlah cara tiap kriteria dikalikan, bukan dijumlah.')
section('Penerapan Permutasi dan Kombinasi','Memilih teknik berdasar makna masalah.','Dalam sebuah kelas ada pemilihan 3 anggota tim dan pemilihan ketua-wakil-sekretaris. Keduanya menggunakan 3 orang. Mengapa jumlah kemungkinannya berbeda?')
L('Identifikasi strategi pencacahan','apakah urutan penting;pernyataan soal;aturan campuran;cek duplikasi',
 'Langkah paling penting dalam pencacahan adalah menerjemahkan cerita menjadi pertanyaan: memilih alternatif, melakukan tahap, menyusun posisi, atau memilih anggota? Daripada langsung mencari rumus, tuliskan dua hasil contoh dan tanyakan apakah mereka dianggap berbeda.',
 '“Ani ketua, Budi wakil” berbeda dengan “Budi ketua, Ani wakil”; tetapi tim {Ani,Budi} sama saja.',
 'Urutan penting → permutasi; urutan tak penting → kombinasi.',
 'Dari 5 orang, apakah menghitung 2 jabatan (ketua dan wakil) memakai 5P2 atau 5C2?',
 'Dua jabatan mempunyai peran berbeda;Menukar orang di kedua jabatan menciptakan hasil berbeda;Gunakan 5P2=5×4=20.',
 '5P2 = 20', 'Memilih 3 anggota tim dari 7 siswa tanpa jabatan memakai ...', ['7P3','7C3','7!'],1,'Karena urutan anggota tim tidak penting, gunakan kombinasi.',
 'Rumus yang benar dipilih dari makna masalah, bukan dari sekadar angka n dan r.')
L('Masalah pencacahan kontekstual','jadwal kegiatan;kombinasi menu;susunan acara;syarat tidak berulang',
 'Masalah nyata sering menggabungkan beberapa aturan. Pecah menjadi tahap-tahap kecil, cari jumlah cara setiap tahap, dan cek apakah suatu pilihan boleh digunakan lebih dari sekali. Jika tidak boleh, jumlah pilihan tahap berikutnya berkurang.',
 'Kode dua angka dari 1,2,3 tanpa pengulangan: setelah memilih angka pertama, hanya dua angka tersisa.',
 'Tanpa pengulangan: n×(n−1) untuk dua posisi dari n simbol.',
 'Berapa kode dua digit berbeda yang dapat dibuat dari angka 1, 2, 3, 4?',
 'Digit pertama memiliki 4 pilihan;Digit kedua harus berbeda, tersisa 3 pilihan;Jumlah = 4×3 = 12 kode.',
 '12 kode', 'Kode dua huruf dari A, B, C tanpa pengulangan berjumlah ...', ['3','6','9'],1,'Pilihan pertama 3; kedua 2; total 3×2 = 6.',
 'Syarat “boleh berulang” mengubah hasil menjadi n×n untuk dua posisi.')

chapter('Peluang',
 'Saat melempar koin atau dadu, kita tidak bisa memastikan hasil berikutnya. Namun, kita tetap dapat menghitung seberapa mungkin sebuah kejadian terjadi.',
 'Peluang adalah ukuran kemungkinan, bukan jaminan hasil. Seluruh model teoretis perlu menjelaskan asumsi, terutama apakah semua hasil sama mungkin.',
 'Proyek 4 · Apakah permainan kita adil?',
 ['Rancang permainan kelas yang memakai dua koin atau satu dadu.','Tulis seluruh kemungkinan hasil dan peluang menang tiap pemain.','Lakukan atau simulasikan minimal 100 percobaan lalu catat frekuensi.','Bandingkan peluang teoretis dengan frekuensi relatif dan usulkan perubahan aturan agar lebih adil.'],
 photos['peluang'],'Foto Zhuo Cheng you / Unsplash')
section('Percobaan Acak dan Ruang Sampel','Menjelaskan hasil yang mungkin sebelum menghitung peluang.','Dua kali melempar koin memiliki empat urutan hasil. Mengapa hasil A-G berbeda dari G-A meskipun sama-sama satu angka dan satu gambar?')
L('Konsep percobaan acak','hasil percobaan;kejadian;ruang sampel;titik sampel',
 'Percobaan acak adalah kegiatan yang hasil pastinya belum diketahui sebelum dilakukan, meskipun daftar hasil yang mungkin bisa dijelaskan. Ruang sampel (S) memuat semua hasil; kejadian A adalah kumpulan hasil yang ingin diperhatikan.',
 'Ketika memutar roda undian, kamu tidak tahu angka yang berhenti, tetapi tahu daftar angka yang tercantum.',
 'S = kumpulan semua hasil mungkin; A adalah bagian dari S.',
 'Sebuah dadu enam sisi bernomor 1 sampai 6 dilempar. Tentukan S dan kejadian A: keluar angka genap.',
 'Ruang sampel S={1,2,3,4,5,6};Angka genap dari daftar itu: 2, 4, 6;Jadi A={2,4,6}.',
 'S={1,2,3,4,5,6} dan A={2,4,6}', 'Ruang sampel untuk satu koin biasa adalah ...', ['{angka, gambar}','{1,2,3}','{angka saja}'],0,'Satu koin memiliki dua sisi: angka dan gambar.',
 'Ruang sampel harus mencakup semua hasil yang mungkin, bukan hanya hasil yang diharapkan.')
L('Menentukan ruang sampel','metode daftar;diagram pohon;tabel pasangan;jumlah hasil',
 'Jika ada dua percobaan, catat hasil sebagai pasangan terurut. Diagram pohon membantu memastikan tidak ada hasil yang terlewat. Pada dua koin, pasangan A-G dan G-A termasuk hasil berbeda apabila urutan lemparan diperhatikan.',
 'Memilih baju lalu celana bisa digambar sebagai cabang: tiap baju bercabang ke semua pilihan celana.',
 'Untuk percobaan bertahap independen dengan m dan n hasil, total pasangan m×n.',
 'Dua koin A/G dilempar. Berapa titik sampel dan apa saja?',
 'Koin pertama: A atau G;Untuk setiap hasil, koin kedua: A atau G;Daftar lengkap: AA, AG, GA, GG — empat hasil.',
 '4 titik sampel: AA, AG, GA, GG', 'Dua dadu enam sisi memiliki banyak pasangan hasil ...', ['12','36','6'],1,'Enam kemungkinan dadu pertama × enam kemungkinan dadu kedua = 36.',
 'Dalam pasangan hasil, urutan sering penting; jangan langsung menggabungkan AG dan GA.')
section('Peluang Suatu Kejadian','Menerjemahkan banyak hasil menjadi ukuran kemungkinan.','Apakah peluang muncul angka 6 pada dadu adalah 1/6 karena ada enam sisi saja, atau ada asumsi yang harus disebut?')
L('Konsep peluang','angka 0 hingga 1;kejadian pasti dan mustahil;hasil sama mungkin;persentase peluang',
 'Peluang adalah ukuran kemungkinan. Nilai 0 berarti mustahil dan nilai 1 berarti pasti. Jika semua hasil sama mungkin, peluang suatu kejadian diperoleh dengan membandingkan banyak hasil yang memenuhi kejadian terhadap seluruh hasil.',
 'Dalam kantong ada 2 kelereng merah dan 3 biru yang serupa ukuran; peluang merah lebih kecil karena pilihannya lebih sedikit.',
 '0 ≤ P(A) ≤ 1; bila sama mungkin, P(A)=n(A)/n(S).',
 'Sebuah kantong berisi 2 bola merah dan 3 bola biru yang identik ukurannya. Berapa peluang mengambil merah?',
 'Jumlah bola seluruhnya = 2+3=5;Ada 2 hasil merah dari 5 bola;P(merah)=2/5=0,4=40%.',
 '2/5 atau 40%', 'Peluang kejadian yang pasti adalah ...', ['0','1','1/2'],1,'Peluang 1 berarti kejadian itu selalu terjadi dalam model.',
 'Rumus banyak hasil dibagi total hanya sah bila hasil-hasil dasar sama mungkin.')
L('Peluang dan komplemen','kejadian bukan A;rumus komplemen;peluang tidak terjadi;penggunaan untuk kasus banyak',
 'Komplemen A berarti “semua hasil selain A”. Karena sebuah hasil pasti masuk A atau bukan A, total kedua peluang itu 1. Cara komplemen berguna saat menghitung “setidaknya satu” karena kebalikannya “tidak ada sama sekali” mungkin lebih mudah.',
 'Jika peluang hujan menurut model 30%, peluang tidak hujan pada saat yang sama adalah 70%.',
 'P(bukan A) = 1 − P(A).',
 'Pada dadu biasa, peluang muncul 6 adalah 1/6. Berapa peluang tidak muncul 6?',
 'P(muncul 6)=1/6;P(tidak muncul 6)=1−1/6;Hasil 5/6.',
 '5/6', 'Jika P(A)=0,25, maka P(bukan A)= ...', ['0,75','0,25','1,25'],0,'1−0,25=0,75.',
 'Komplemen bukan lawan yang asal dipilih: ia harus mencakup semua hasil di luar A.')
section('Frekuensi Harapan','Menghubungkan perhitungan peluang dengan percobaan.','Jika peluang teoretis suatu kejadian adalah 1/2 dan percobaan dilakukan 10 kali, apakah pasti muncul tepat lima kali?')
L('Peluang eksperimental','frekuensi kejadian;frekuensi relatif;peluang teoretis;fluktuasi sampel',
 'Peluang teoretis dihitung dari model. Peluang eksperimental diperoleh dengan membagi banyak kejadian yang benar-benar muncul dengan banyak percobaan. Pada jumlah percobaan kecil, hasil eksperimental bisa berbeda cukup jauh dari nilai teoretis.',
 'Melempar koin 10 kali bisa menghasilkan 7 angka dan 3 gambar, meski pada koin seimbang peluang masing-masing 1/2.',
 'Frekuensi relatif = banyak kemunculan / total percobaan.',
 'Koin dilempar 20 kali; sisi angka muncul 12 kali. Berapa frekuensi relatif angka?',
 'Banyak muncul angka=12;Total percobaan=20;Frekuensi relatif=12/20=0,6=60%.',
 '0,6 atau 60%', 'Jika merah muncul 15 kali dari 50 pengambilan, frekuensi relatifnya ...', ['0,3','0,5','3'],0,'15÷50=0,3.',
 'Frekuensi relatif dari 20 percobaan bukan bukti bahwa peluang teoretis selalu 0,6.')
L('Frekuensi harapan kejadian','hasil rata-rata yang diharapkan;rumus nP;perbedaan ramalan dan jaminan;perbandingan data',
 'Frekuensi harapan adalah banyak kemunculan yang diperkirakan secara rata-rata jika sebuah percobaan dilakukan berulang. Nilainya tidak selalu sama dengan hasil aktual dari satu rangkaian percobaan.',
 'Jika rata-rata satu dari empat pelanggan membeli produk, dari 100 pengunjung kita mengharapkan sekitar 25 pembeli, bukan menjamin tepat 25.',
 'Frekuensi harapan Fh = n × P(A).',
 'Dadu seimbang dilempar 60 kali. Berapa frekuensi harapan muncul angka 6?',
 'P(angka 6)=1/6;Jumlah percobaan n=60;Fh=60×1/6=10.',
 '10 kali (harapan)', 'Peluang 1/4 untuk 40 percobaan memberi frekuensi harapan ...', ['4','10','20'],1,'40×1/4 = 10.',
 'Frekuensi harapan bukan kepastian hasil percobaan yang sebenarnya.')
section('Peluang Kejadian Majemuk','Memahami peristiwa yang melibatkan dua syarat atau lebih.','Pada dadu, kejadian genap dan lebih dari 3 mempunyai irisan. Mengapa peluang “genap atau >3” tidak cukup menjumlahkan keduanya?')
L('Gabungan dan irisan kejadian','A atau B;A dan B;diagram Venn;rumus gabungan umum',
 'Gabungan A∪B berarti hasil termasuk A atau B atau keduanya. Irisan A∩B berarti hasil memenuhi dua syarat sekaligus. Jika langsung menjumlahkan P(A) dan P(B), hasil irisan terhitung dua kali, sehingga perlu dikurangi sekali.',
 'Siswa yang ikut klub musik atau klub olahraga bisa tergabung di kedua klub; jangan dihitung sebagai dua orang.',
 'P(A∪B)=P(A)+P(B)−P(A∩B).',
 'Pada dadu, A={2,4,6} dan B={4,5,6}. Berapa P(A∪B)?',
 'P(A)=3/6;P(B)=3/6;Irisan A∩B={4,6} sehingga P(irisan)=2/6;P(gabungan)=3/6+3/6−2/6=4/6=2/3.',
 '2/3', 'Simbol A∩B berarti ...', ['A atau B','A dan B sekaligus','Bukan A'],1,'Irisan adalah hasil yang masuk ke A sekaligus B.',
 'Pernyataan “atau” pada matematika biasanya juga mencakup hasil yang memenuhi keduanya.')
L('Analisis kejadian majemuk','tabel dua arah;peluang irisan;gabungan;menafsirkan kata dan atau',
 'Soal data dapat disajikan dalam tabel. Untuk peluang dari sebuah populasi, penyebutnya adalah jumlah seluruh objek yang dijadikan ruang sampel. “Dan” menunjukkan sel persilangan dua kategori; “atau” menunjukkan penggabungan kategori.',
 'Catatan perpustakaan membedakan siswa kelas XI/XII dan suka novel/komik; sel satu kategori dapat dibaca sebagai irisan.',
 'P(A∩B)=jumlah anggota yang memenuhi keduanya / jumlah seluruh anggota, jika tiap anggota sama mungkin dipilih.',
 'Dari 20 siswa, 8 suka sepak bola, 7 suka bulu tangkis, dan 3 suka keduanya. Berapa yang suka minimal salah satu?',
 'Jumlah sepak bola =8;Jumlah bulu tangkis=7;Kurangi yang terhitung dua kali: 8+7−3=12 siswa.',
 '12 siswa', 'Jika 6 orang suka A, 5 suka B, 2 suka keduanya, yang suka A atau B ada ...', ['11','9','3'],1,'6+5−2=9.',
 'Jangan menjumlahkan dua kelompok tanpa mengecek apakah ada anggota yang masuk keduanya.')
section('Kejadian Saling Lepas','Mengenali kejadian yang tidak mungkin bersamaan.','Pada satu lemparan dadu, apakah muncul angka genap dan muncul angka ganjil bisa terjadi sekaligus? Bagaimana dengan muncul angka genap dan lebih dari 3?')
L('Konsep kejadian saling lepas','irisan kosong;perbedaan dengan bebas;aturan gabungan khusus;contoh dadu',
 'Dua kejadian saling lepas tidak dapat terjadi secara bersamaan pada satu percobaan. Contohnya, dalam satu lemparan dadu, hasil 1 dan hasil 6 tidak mungkin muncul sekaligus. Karena irisannya nol, peluang gabungan cukup dijumlahkan.',
 'Satu tiket bernomor hanya dapat memiliki satu nomor pemenang utama dalam satu pengundian.',
 'Jika A∩B=∅, P(A∪B)=P(A)+P(B).',
 'Pada dadu biasa, peluang muncul 1 atau 6 adalah ...',
 'P(1)=1/6;P(6)=1/6 dan keduanya tidak dapat muncul bersama;P(1 atau 6)=1/6+1/6=2/6=1/3.',
 '1/3', 'Kejadian muncul angka 2 dan angka 5 pada satu lemparan dadu bersifat ...', ['Saling lepas','Selalu bersama','Saling bergantung secara positif'],0,'Satu dadu tidak mungkin sekaligus menunjukkan 2 dan 5.',
 'Saling lepas tidak sama dengan saling bebas; kedua konsep memiliki arti berbeda.')
L('Penerapan kejadian saling lepas','kategori tidak beririsan;model satu percobaan;rumus penjumlahan;pemeriksaan total',
 'Periksa dahulu apakah dua hasil mungkin bersamaan. Pada satu pengambilan kartu, kartu tidak bisa sekaligus menjadi hati dan sekop. Maka keduanya saling lepas pada satu kartu. Namun aturan akan berbeda jika mengambil beberapa kartu.',
 'Memilih satu menu sebagai makanan atau minuman tanpa kategori tumpang tindih memakai logika penjumlahan.',
 'Jika saling lepas: P(A∪B)=P(A)+P(B) dan hasil ≤1.',
 'Kotak berisi 4 bola merah, 3 biru, dan 3 hijau. Peluang mengambil merah atau biru dalam satu kali pengambilan?',
 'Total bola=10;Merah dan biru tak mungkin terjadi sekaligus pada satu bola;P=4/10+3/10=7/10.',
 '7/10', 'Satu kartu dari 52 kartu standar: peluang hati atau sekop adalah ...', ['1/2','1/4','1/13'],0,'Ada 13 kartu hati dan 13 sekop; (13+13)/52=1/2.',
 'Periksa apakah ruang sampel satu pengambilan atau beberapa pengambilan.')
section('Kejadian Saling Bebas','Memahami kejadian satu tidak mengubah peluang yang lain.','Mengapa hasil lemparan koin pertama tidak mengubah peluang hasil lemparan koin kedua pada dua lemparan koin ideal?')
L('Konsep independensi','arti saling bebas;peluang irisan;beda bebas dan lepas;percobaan ulang',
 'Saling bebas berarti informasi tentang kejadian pertama tidak mengubah peluang kejadian kedua. Dua lemparan koin ideal merupakan contoh. Jika dua kejadian bebas, peluang keduanya terjadi diperoleh dengan perkalian peluang masing-masing.',
 'Kondisi cuaca hari ini tidak memengaruhi sisi sebuah koin ideal yang dilempar di dalam kelas.',
 'Jika A dan B bebas, P(A∩B)=P(A)×P(B).',
 'Dua koin seimbang dilempar. Berapa peluang keduanya menunjukkan angka?',
 'P(angka koin pertama)=1/2;P(angka koin kedua)=1/2 dan bebas;P(keduanya angka)=1/2×1/2=1/4.',
 '1/4', 'Dua lemparan koin seimbang yang terpisah dianggap ...', ['Saling bebas','Pasti sama hasil','Saling lepas'],0,'Hasil pertama tidak mengubah peluang hasil kedua.',
 'Dua kejadian yang saling lepas dan sama-sama berpeluang positif justru tidak bebas.')
L('Penerapan kejadian saling bebas','koin dan dadu;pemilihan dengan pengembalian;diagram pohon;uji independensi',
 'Pengambilan dengan pengembalian dapat menghasilkan percobaan independen ketika komposisi benda kembali seperti semula dan proses pengambilannya acak. Jika tanpa pengembalian, isi kantong berubah sehingga peluang tahap berikutnya biasanya ikut berubah.',
 'Ambil kelereng, lihat warnanya, lalu kembalikan dan aduk lagi: peluang pada percobaan kedua tetap sama.',
 'P(A dan B)=P(A)P(B) untuk peristiwa bebas.',
 'Kantong berisi 2 bola merah dan 3 biru. Ambil satu bola, kembalikan, lalu ambil lagi. Peluang dua kali merah?',
 'P(merah setiap pengambilan)=2/5;Karena dikembalikan dan diacak, peluang kedua tetap 2/5;P(keduanya merah)=2/5×2/5=4/25.',
 '4/25', 'Dua kali pengambilan dengan pengembalian dari kantong yang komposisinya tetap cenderung ...', ['Bebas','Saling lepas','Pasti sama'],0,'Pengembalian menjaga kondisi peluang dasar setiap percobaan.',
 'Tanpa pengembalian, peluang langkah kedua tidak sama karena jumlah benda dalam kantong berubah.')
section('Peluang Bersyarat','Menghitung peluang setelah mendapat informasi tambahan.','Diketahui sebuah kartu yang diambil adalah kartu merah. Apakah peluang kartu hati masih 13/52? Mengapa ruang sampelnya berubah?')
L('Konsep peluang bersyarat','informasi B sudah terjadi;ruang sampel baru;notasi P(A|B);rumus kondisional',
 'Peluang bersyarat mengukur peluang A ketika kita sudah mengetahui B terjadi. Artinya, ruang sampel dipersempit hanya pada hasil B. Dari hasil B itulah kita menghitung bagian yang juga memenuhi A.',
 'Jika tahu seseorang sudah masuk perpustakaan, peluang dia meminjam buku dihitung dari pengunjung perpustakaan, bukan dari semua siswa sekolah.',
 'P(A|B)=P(A∩B)/P(B), untuk P(B)>0.',
 'Dari 10 siswa, 6 perempuan dan 4 laki-laki. Di antara 6 perempuan, 2 memakai kacamata. Jika diketahui siswa yang dipilih perempuan, peluang berkacamata?',
 'Informasi “perempuan” membatasi ruang sampel menjadi 6 siswa;Dari 6 siswa ini, 2 berkacamata;P(kacamata | perempuan)=2/6=1/3.',
 '1/3', 'Jika diketahui siswa terpilih berasal dari 8 anggota klub dan 3 di antaranya juara, peluang juara adalah ...', ['3/8','3/20','8/3'],0,'Penyebutnya kini 8 anggota klub yang sudah diketahui.',
 'Peluang bersyarat membutuhkan penyebut P(B)>0 dan tidak selalu sama dengan peluang awal P(A).')
L('Penerapan peluang bersyarat','pengambilan tanpa pengembalian;tabel dua arah;diagram pohon;hubungan dengan bebas',
 'Tanpa pengembalian, hasil pengambilan pertama memengaruhi komposisi benda sebelum pengambilan kedua. Cara sederhana adalah memperbarui jumlah benda dan jumlah total pada langkah kedua. Diagram pohon membantu menuliskan percabangan dengan jelas.',
 'Dari kotak 3 kelereng merah dan 2 biru, setelah satu merah diambil tanpa dikembalikan, sekarang tersisa 2 merah dari 4.',
 'P(A dan B)=P(A)×P(B|A), jika P(A)>0.',
 'Kotak berisi 3 merah dan 2 biru. Dua bola diambil berturut-turut tanpa pengembalian. Berapa peluang keduanya merah?',
 'P(merah pertama)=3/5;Setelah merah pertama keluar, tersisa 2 merah dari 4 bola → P(merah kedua|pertama merah)=2/4;P(keduanya merah)=3/5×2/4=3/10.',
 '3/10', 'Setelah mengambil 1 merah dari 3 merah dan 2 biru tanpa pengembalian, peluang merah berikutnya ...', ['3/5','2/4','2/5'],1,'Sekarang jumlah merah 2 dan total 4.',
 'Kesalahan umum: tetap memakai 3/5 pada pengambilan kedua yang tanpa pengembalian.')
section('Simulasi dan Pengambilan Keputusan','Menilai model dengan data dan menyadari ketidakpastian.','Dua permainan sama-sama menawarkan peluang menang 1/2. Apakah keduanya pasti menghasilkan pemenang seimbang setelah hanya empat putaran?')
L('Simulasi probabilitas','percobaan nyata;simulasi spreadsheet;frekuensi relatif;jumlah ulangan',
 'Simulasi menjalankan percobaan berulang untuk membandingkan hasil dengan teori. Kita bisa memakai koin nyata atau rumus acak pada spreadsheet. Simulasi sangat berguna untuk melihat variasi: dua kelompok dengan aturan sama dapat memperoleh hasil berbeda.',
 'Di kelas, dua kelompok melempar koin masing-masing 20 kali; persentase angka mereka tidak harus sama.',
 'Frekuensi relatif = jumlah kejadian ÷ jumlah percobaan.',
 'Dari 100 lemparan koin, 53 menghasilkan angka. Bandingkan dengan peluang teori 1/2.',
 'Frekuensi relatif angka=53/100=0,53;Peluang teoretis angka=1/2=0,50;Perbedaannya 0,03 atau 3 poin persentase.',
 'Frekuensi relatif 53%; teori 50%', 'Apakah 50 percobaan koin seimbang selalu menghasilkan tepat 25 angka?', ['Ya','Tidak','Hanya jika memakai kalkulator'],1,'Hasil percobaan acak bisa menyimpang dari nilai harapan.',
 'Simulasi tidak membuktikan kepastian satu hasil; ia membantu memahami pola jangka panjang.')
L('Penalaran dan evaluasi probabilitas','kekeliruan peluang;keadilan permainan;asumsi model;keputusan berbasis risiko',
 'Dalam permainan adil sederhana, kedua pemain memiliki kesempatan menang yang sama menurut aturan. Untuk menilai keadilan, hitung dulu peluang semua hasil, kemudian lihat apakah aturan membagi peluang itu secara seimbang. Perbedaan hasil beberapa putaran tidak otomatis berarti permainan curang.',
 'Jika satu sisi koin muncul lima kali berturut-turut, lemparan berikutnya pada koin ideal tetap punya peluang 1/2 untuk masing-masing sisi.',
 'Pada koin ideal, P(angka pada lemparan berikutnya)=1/2 terlepas dari urutan sebelumnya.',
 'Permainan: pemain A menang jika dadu menunjukkan 1 atau 2; pemain B menang jika 3,4,5,6. Apakah adil?',
 'P(A)=2/6=1/3;P(B)=4/6=2/3;Karena peluang B dua kali peluang A, permainan tidak adil bila hadiah dan syarat sama.',
 'Tidak adil; B mempunyai peluang 2/3', 'Lima kali angka pada koin ideal membuat peluang gambar berikutnya ...', ['Lebih besar dari 1/2','Tetap 1/2','Menjadi 0'],1,'Pada lemparan independen, sejarah tidak mengubah peluang lemparan berikutnya.',
 'Jangan menyimpulkan “sudah lama tidak muncul, berarti sekarang pasti muncul”; itu kekeliruan penjudi.')

assert len(C)==4
assert [len(x['sections']) for x in C]==[6,6,6,8]
assert all(len(s['lessons'])==2 for c in C for s in c['sections'])
for ci,c in enumerate(C,1):
 c['id']=f'bab-{ci}'
 for si,s in enumerate(c['sections'],1):
  s['id']=f'{ci}-{si}'
  for li,l in enumerate(s['lessons'],1):
   l['id']=f'{ci}-{si}-{li}'
   l['code']=f'{ci}.{si}.{li}'
obj={'title':'Matematika Umum Kelas XII SMA/MA — Pendamping Akademik','edition':'Edisi Pembelajaran 2026/2027','chapters':C,'sources':[
  {'name':'Matematika untuk SMA/MA/SMK/MAK Kelas XII, Edisi Revisi 2025 (Kemendikdasmen)','url':'https://buku.kemendikdasmen.go.id/katalog/matematika-untuk-smamasmkmak-kelas-xii-edisi-revisi'},
  {'name':'Buku Siswa Kelas XII Revisi 2025 (PDF)','url':'https://static.sc.cloudapp.web.id/content/pdf/bukuteks/kurikulum21/Matematika_BS_KLS_XII_Rev.pdf'},
  {'name':'Panduan Mata Pelajaran Matematika Fase A–F (Kemendikdasmen, 2025)','url':'https://repositori.kemendikdasmen.go.id/33608/'},
  {'name':'Lisensi Unsplash','url':'https://unsplash.com/license'}],
 'photos':[
 {'credit':'CHUTTERSNAP','url':'https://unsplash.com/de/fotos/bucher-im-bucherregal-b2Rmlyz7n3I'},
 {'credit':'Jakub Żerdzicki','url':'https://unsplash.com/photos/a-person-sitting-at-a-desk-with-a-calculator-and-a-notebook-LNnmSumlwO4'},
 {'credit':'One Pixel','url':'https://unsplash.com/fr/photos/une-rangee-de-crayons-de-couleur-alignes-sur-un-fond-blanc-47JLCB-ZL_0'},
 {'credit':'Zhuo Cheng you','url':'https://unsplash.com/photos/white-dice-on-brown-wooden-table-2WE_V_dh0B0'}]}
(ROOT/'materi.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
print('chapters',len(C),'subbab',sum(len(c['sections']) for c in C),'materi',sum(len(s['lessons']) for c in C for s in c['sections']))
print('materi json size', (ROOT/'materi.json').stat().st_size)
