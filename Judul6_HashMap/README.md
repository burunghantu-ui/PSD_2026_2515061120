# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana untuk menyimpan data pasien VIP ke dalam suatu daftar dengan urutan acak acak yang berdasarkan kode uniik yang dimiliki pasien, yang mana pada dafatr tersebut berisi kode unik, nama serta penyakit yang sedang di derita pasien, dalam program ini klinik dapat menambahkan pasien ke daftar, mencari dan menghapus pasien tertentu berdasarkan kode unik mereka, dan melihat keseluruhan pasien yang ada, untuk saat ini klinik hanya dapat menampung total 10 pasien VIP.

Demi dapat menyimpan data secara efisien kkami menggunakan metode HashMap Open Addressing, yang mana metode ini akan menyimpan nama pasien ke dalam daftar dimana urutannya akan di tentukan oleh fungsi hash yang mengubah kode unik pasien kedalam indeks yang nantinya akan menjadi nomor urut pasien. kami menggunakan jenis Open Addressing, karena berbeda dengan HashMap Separate chaining yang dalam satu indeks dapat memuat lebih dari 1 informasi pasein, open addresing memiliki strategi yang memastikan setap indeks hanya memiliki satu informasi pasien sehingga mengurangi adanya collisiond dalam data dan memastikan bahwa jumllah pasien yang terdapat dalam daftar tidak lebih dari 10.

Menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada, selain itu perulangan for juga digunakan dalam mengecek sebanyak data pasien untuk menemukan nama pasien yang di cari. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

# Source Code
<img width="257" height="101" alt="image" src="https://github.com/user-attachments/assets/01c4c67a-c02d-413f-82d5-52c6f23bf0d3" />

baris 1 terdapat class bernama slotState yang mencakup baris 2-4 dan di gunakan untuk mendeklarasikan nilai EMPTY(2), OCCUPIED(3), dan DELETED(4)

<img width="453" height="129" alt="image" src="https://github.com/user-attachments/assets/15a3c40e-38b9-49d3-bc3c-58b43d385411" />

baris 7 terdapat class Entry yang mmencakup baris 8-11, dimana pada barsis 8 terdapat fungsi init yang digunakan untuk mengosongkan key(9), value(10), dan state(11) itu sendiri

<img width="624" height="105" alt="image" src="https://github.com/user-attachments/assets/f011499f-e466-402d-92aa-06b027a4eabf" />

baris 14, terdapat kelas hashmap open addresing yang mencakup baris 15-74 dimana di dalamnya terdapat berbagai fungsi yang dapat digunakan untuk kelas atau variabel yang berisi kelas itu sendiri

baris 15 terdapat fungsi init yang di gunakan untuk mendefinisikan dan mengisi atribut awalnya, dimana pada baris 16 terdapat pendefinisian bahwa self.SIZE itu bernilai size (atau 10)

baris 17, variable self.table memanggil kelas entri sekaligus perulangan for untuk mengosongkan seluruh tempat yang tersedia pada tabel terlebih dahulu

<img width="581" height="47" alt="image" src="https://github.com/user-attachments/assets/3d3732b5-b593-4376-a3e1-62649a2ee57d" />

baris 19, terdapat fungsi hash function yang mana digunakan untuk mengubah key menjadi nilai tertentu yang akan menjadi indeks untuk menyimpan data key 

baris 20, merupakan pengembalian nilai berupa hasil perubahan key menjadi suatu angka indeks

<img width="646" height="217" alt="image" src="https://github.com/user-attachments/assets/41aa0130-a4ea-4333-b95b-434066e4189c" />

baris 22, terdapat fungsi  insert yang berguna untuk menambahkan data ke daftar yanag mana fungsi ini mencakup baris 23-46.

baris 23, terdapat variabel idx yang akan menyimpan hasil hash function dengan memanggil fungsi tersebut

baris 24, terdarpat variabel yang menyatakan bahwa aksi deleted pertama bernilai -1 atau belum pernah di lakukan

baris 25, terdapat perulangan for yang akan di gunakan untuk memeriksa seluruh tempat atau daftar, perulangan ini mencakup baris 26-40

baris 26, terdapat variabel i yang menyimpan nilai yang digunakan untuk memastikan tidak keluar dari jumlah pengecekan

baris 27, terdapat percabangan if dengan kondisi jika table dengan indeks ke i tersebut telah terisi maka akan mengeksekusi baris 28-30

baris 28, terdapat percabangan kembali dimana jika key dari data indeks table ke i sama  dengan key yang dimasukkan user maka akan mengeksekusi baris 29-30 akan di eksekusi dimaana baris 29 akan mengganti value data sebelumnya pada indeks tabel tersebut dengan value baru yang di masukkan oleh user dan mengembalikan niLai True (30)

<img width="638" height="246" alt="image" src="https://github.com/user-attachments/assets/5a8e4ea9-4213-4705-b508-c4ae244de5f5" />

baris 31 merupakan lanjutan dari kondisi pada baris 27 yang mana jika data dari tabel indeks ke i ternyata pernah di hapus sebelumnya maka baris 32-33 akan diekseksui

baris 32 terdapat percabangan dimana jika first deleted pada saat itu bernilai -1 maka akan mengeksekusi baris 33 yang akan menggantikan nilai firts deleted dengan nilai dari i

baris 34, merupakan lanjutan dari percabangan sebelumnya di baris 31 yang mana akan dijalankan jika kondisi kedua percabangan sebelumnya tidak terpenuhi maka akan mengeksekusi baris 35-40

baris 35, merupakan percabangan baru dimana jika first deleted tidak bernilai -1 maka akan mengeksekusi baris 36 yang mana merubah nilai i menjadi nilai first deleted

baris 37, merupakan pergantian nilai key pada indeks ke i pada table menjadi nilai key yang di masukkan pengguna, begitu pula pada baris 38 yang mengubah nilai value indeks ke i table menjadi value yang di masukkan oleh user, lalu pada baris 39 merupakan pemberian status bahwa pada indeks tersebut telah menyimpan data, dan pada baris 40 merupakan pengembalian nilai true 

<img width="691" height="150" alt="image" src="https://github.com/user-attachments/assets/b2350f7f-217f-4385-80ab-42270916ffc7" />

baris 41, akan dikesekusi ketika tidak kondisi percabangan dalam perulangan for telah dieksekusi tanpa ada pengembalian nilai ataupun ketika tidak terpenuhi dan percabangannya tidak memiliki kondisi lain atau 'else'. dimana pada baris ini terdapat percabangan dengan kondisi dimana jika first_deleted bukan bernilai -1 maka akan mengeksekusi baris 42-45

baris 42, merupakan pergantian nilai key pada indeks ke first_deleted dengan nilai key yang dimasukkan user, begitu pula pada baris 43 yang mengganti nilai valuenya dengan value yang di masukkan oleh user, lalu pada baris 44, state pad indeks tersebut akan di berikan status telah diisi lalu dikembalikan nilai True pada baris 45.

baris 46 merupakan pengembalian nilai false ketika tidak ada pengembalian nilai yang di lakukan sebelumnya.

<img width="891" height="220" alt="image" src="https://github.com/user-attachments/assets/8722ef48-3965-42ce-893f-af29986d86e7" />

baris 48, terdapat fungsi search yang akan di gunakan untuk mencari informasi psaien berdasarkan kode unik dimana mencakup baris 49-56

baris 49, terdapat variabel idx yang akan di gunakan untuk menyimpan hasil nilai function hash dengan memanggil fungsi tersebut

baris  50, terdapat perulangan for yang akan melakukan looping sebanyak jumlah size daftar pasien (yaitu 10), dimana perulangan ini mencakup baris 51-56

baris 51, terdapat variabel i yang menyimpan nilai yang digunakan untuk memastikan tidak keluar dari jumlah pengecekan

baris 52, terdapat percabangan dengan kondisi dimana jika  indeks ke i pada table kosong maka akan mengembalikan nilai false dan none (53)

baris 54, terdapat percabangan dengan kondisi jika data pada indeks ke i pada table daftar telah terisi data dan nilai key nya sama dengan yang dimasukkan user maka akan mengeksekusi baris 55 yang akan mengembalikan nilai True dan isi data indeks ke i dari tabel daftar

baris 56, terdapat pengembalian nilai false dan none yang akan dieksekusi ketika sebelumnya pada fungsi ini belum melakukan pengembalian nilai.

<img width="490" height="147" alt="image" src="https://github.com/user-attachments/assets/2bf68c84-d724-4531-8627-44317fba5f3c" />

baris 58, terdapat fungsi remove untuk menghapus data pada indeks tertentu yang mana fungsi ini mencakup baris 59-63

baris 59, terdapat variabel bool dan entry yang akan menampung pengembalian nilai dari fungsi search yang di panggil

baris 60 terdapat percabangan dimana jika entry bernilai none dan bool bernilai false maka akan mengeksekusi baris 61 yang akan mengembalikan nilai False

baris 62, merupakan pendefinisian bahwa data entry tekah dihapus lalu pada baris 63 akan di lakukan pengembalian nilai True

<img width="730" height="245" alt="image" src="https://github.com/user-attachments/assets/af86c902-e0cd-48ba-b858-62c7f70ae26d" />

baris 65, terdapat fungsi display yang berguna untuk menampilkan keseluruhan daftar, dimana fungsi ini mencakup baris 66-74

baris 66, akan menampilkan "daftar informasi antrian pasien"

baris 67, terdapat perulanagn for yang mencakup baris 68-74

baris 68, akan menampilkan urutan antrian pada daftar pasien atau table dengan penambahan +1 untuk menghindari antrian 0

baris 69, terdapat percabangan dengan kondisi dimana jika status data pada indeks ke i table sama dengan empty atau kosong maka akan mengekseskusi baris 70 yang mana akan menampilkan empty

baris 71, merupakan lanjutan percabangan sebelumnya dengan kondisi jika status data pada indeks ke i di daftar tabel sama dengan deleted atau telah dihapus sebelumya maka akan mengeksesuki baris 72 yang akan menampilkan "DELETED"

baris 73, merupakan lanjutan dari percabangan sebelumnya dimana jika tidak ada kondisi yang terpenuhi sebelumnya maka akan mengeksekusi baris 74 yang mana akan menampilkan key serta value data dari indeks ke i daftar table

<img width="443" height="144" alt="image" src="https://github.com/user-attachments/assets/fae02616-425b-4072-b4bb-3b8b59499ccc" />

baris 76, terdapat fungsi menu mencakup baris 77-81 yang mana berfungsi untuk menampilkan menu berupa apa saja yang user dapat lakukan dengan program ini

<img width="520" height="127" alt="image" src="https://github.com/user-attachments/assets/1edd1145-72bb-4a9c-bb4e-bce6f1fb7e50" />

pada baris 84 terdapat fungsi main yang didalamnya meruoakan logika inti program, dimana mencakup baris 85-145

baris 85-88 merupakan memasukkan data pasien ke dalam daftar dengan memanggil fungsi insert

<img width="773" height="80" alt="image" src="https://github.com/user-attachments/assets/889e59ff-0d71-4e25-a002-f5eb07b1264a" />

baris 90-92 merupakan judul program yang di guakan untuk  mempercantik program saat di jalankan

<img width="498" height="268" alt="image" src="https://github.com/user-attachments/assets/5de19747-9020-46f3-aa02-bce964ed8612" />

baris 94 terdapat perulangan while yang mana akan terus mengeksekusi baris 95-145 sampai kondisi break terpenuhi

baris 95, terdapat pemanggilan menu yang mana akan menampilkan pilihan aksi ke pada user

baris 96 terdapat perulangan while yang digunakan untuk mengulangi permintaan input setiap kali user salam memasukkan tipe data input di baris 98

baris 97 terdapat exception handling try yang digunakan untuk memastikan input pil user pada baris 98 berupa angka, ketika user memasukkan input angka maka selanjutanya baris 99 akan dieksekusi yang mana akan menghentikan perulangan di baris 96 dan masuk ke kode selanjutnya di baris 103, sebaliknya jika user memasukkan data selain integer atau angka maka akan mengeksekusi baris 100 dan menampilkan baris 101 lalu meminta kembali input user di baris 98

baris 103, merupakan percabangan dengan kondisi dimana jika input pil yang di masukkan user bernilai sama dengan 1 maka akan mengeksekusi baris 104 yang memanggil fungsi display dan menampilkan daftar informasi seluruh indeks pada daftar

<img width="844" height="221" alt="image" src="https://github.com/user-attachments/assets/ba46523a-bc38-4f39-b738-b596f4efa885" />

baris 105 merupakan lanjutan dari percabangan sebelumnya dimana jika kondisi berupa  pil bernilai sama dengan 2 terpenuhi maka akan diekseksui baris 106-113

baris 106, terdapat perulangan while yang di gunakan untuk memastikan except handling dapat beroperasi dengan lancar

baris 107, terdapat exception handling try yang digunakan untuk memastikan input kode user pada baris 108 berupa angka, ketika user memasukkan input angka maka selanjutanya baris 109 akan dieksekusi yang mana akan menghentikan perulangan di baris 106 dan masuk ke kode selanjutnya di baris 112, sebaliknya jika user memasukkan data selain integer atau angka maka akan mengeksekusi baris 110 dan menampilkan baris 111 lalu meminta kembali input user di baris 108

baris 112, terdapat variabel nilai yang akan meminta user memasukkan value dari kode atau key yang akan di tambahkan ke dalam daftar

baris 113, merupakan penambahan informasi pasien ke daftar dengan memanggil fungsi insert dan memasukkan kode atau key dan value atau nilai yang telah di masukkan user sebelummnya

<img width="794" height="299" alt="image" src="https://github.com/user-attachments/assets/431eb916-d59f-424e-b466-4a3ba62bf80a" />

baris 115 merupakan lanjutan dari percabangan sebelumnya dimana jika kondisi berupa  pil bernilai sama dengan 3 terpenuhi maka akan mengekseksui baris 116-126

baris 116, terdapat perulangan while yang di gunakan untuk memastikan except handling dapat beroperasi dengan lancar

baris 117, terdapat exception handling try yang digunakan untuk memastikan input cari user pada baris 118 berupa angka, ketika user memasukkan input angka maka selanjutanya baris 119 akan dieksekusi yang mana akan menghentikan perulangan di baris 116 dan masuk ke kode selanjutnya di baris 122, sebaliknya jika user memasukkan data selain integer atau angka maka akan mengeksekusi baris 120 dan menampilkan baris 121 lalu meminta kembali input user di baris 118

baris 122, terdapat variabel hasil yang akan menyimpan hasil dari pemanggilan fungsi search

baris 123, terdapat percabangan dengan kondisi dimana jika hasil tidak kosong maka akan mengeksekusi baros 124 yang akan menampilkan informasi pasien

baris 125 adalah percabangan lanjutan dimana ketika kondisi pada baris 123 tidak terpenuhi maka akan mengeksekusi baris 126 yang menyatakan bahwa  pasien tidak di temukan

<img width="784" height="315" alt="image" src="https://github.com/user-attachments/assets/0a25e8e6-8e41-45ee-9a58-78571a477fd2" />

baris 128 merupakan lanjutan dari percabangan sebelumnya dimana jika kondisi berupa pil bernilai sama dengan 4 terpenuhi maka akan mengekseksui baris 129-140

baris 129, terdapat perulangan while yang di gunakan untuk memastikan except handling dapat beroperasi dengan lancar

baris 130, terdapat exception handling try yang digunakan untuk memastikan input cari user pada baris 131 berupa angka, ketika user memasukkan input angka maka selanjutanya baris 132 akan dieksekusi yang mana akan menghentikan perulangan di baris 129 dan masuk ke kode selanjutnya di baris 135, sebaliknya jika user memasukkan data selain integer atau angka maka akan mengeksekusi baris 133 dan menampilkan baris 134 lalu meminta kembali input user di baris 131

baris 135, terdapat variabel bool dan hasil yang mana akan menampung hasil pengembalian nilai degan memanggil fuungsi search

baris 136, terdapat percabangan di mana jika bool bernilai True maka akan mengekseskui baris 137 yang mana akan mengatakan bahwa data dengan key yang di masukkan user telah berhasil di hapus

baris 138 merupakan lanjutan percabangan di baris sebelumnya di mana jika kondisi sebelumnya tidak terpenuhi maka akan mengeksekusi baris 139 yang akan menyatakan bahwa data dengan key yang di cari tidak tersedia

baris 140, merupakan pemanggilan fungsi remove_key yang berguna untuk benar benar menghapus data sesuai dengan key yang di masukkan user.

<img width="528" height="106" alt="image" src="https://github.com/user-attachments/assets/e781eb05-bdab-42af-9595-564ee261cea1" />

baris 142 merupakan lanjutan dari percabangan sebelumnya dimana jika kondisi berupa pil bernilai sama dengan 5 terpenuhi maka akan mengekseksui baris 143 yang mana akan menghentikan perulangan while di baris ke 94

baris 144 merupakan lanjutan percabangan di baris sebelumnya di mana jika kondisi sebelumnya yaitu pil =1 /2/3/4/5tidak terpenuhi maka akan mengeksekusi baris 139 yang akan menyatakan bahwa data dengan key yang di cari tidak tersedia maka baris 145 akan di eksekusi dan  kemmabli meminyta user  memasukkan angka sesuai dengan yang telah diinformasikan di barisan pertama kode ini

<img width="326" height="58" alt="image" src="https://github.com/user-attachments/assets/cec82efb-1113-4272-9725-20a915132529" />

baris 147-148 merupkan pemanggilan dari fungsi utama

# OutPut

<img width="541" height="225" alt="image" src="https://github.com/user-attachments/assets/594d247c-caf0-49c2-8e2e-327919bb4991" />

saat program pertama kali dijalankan, program akan menampilkan judul program sekaligus menu yang dapat dipilih oleh user, selanjutnya program akan meminta user memasukkan pilihan berdasarkan menu yang di tampilkan

<img width="332" height="314" alt="image" src="https://github.com/user-attachments/assets/6471f2bd-75cf-4ec2-b133-5c09a54140b8" />

selanjutnya ketikda user memasukkan angka 1 maka program akan menampilkan daftar antrian pasien baik yang telah terisi, koson, maupun telah di hapus

<img width="263" height="138" alt="image" src="https://github.com/user-attachments/assets/ed9f6453-c0a0-4e3c-b8a1-c8e4c2285a44" />

selanjutnya program akan kembali menampilkan tampilan menu dan permintaan input pilihan kepada user

<img width="654" height="192" alt="image" src="https://github.com/user-attachments/assets/336876fe-a37d-419a-9e5b-8ae4e9eaecca" />

selanjutnyta ketika user memasukkan angka 2, maka program akan meminta kode unik pasien yang ingin ditambahakan dimmana selanjutnya user akan diminta memasukkan nama sekaligus penyakit yang diderita oleh user, setelah user memasukkan kode, nama, serta penyakit user maka program akan kembali menampilkan menu serta permintaan input kepada user

<img width="408" height="114" alt="image" src="https://github.com/user-attachments/assets/46223b89-9db9-4be5-a9d0-4a9a0820db8b" />
ketika user memasukkan angka 3 maka program akan meminta kode unik dari pasien yang ingin di cari, setelahnya ketika pasien dengan kode unik yang dimasukkan terdapat dalam daftar maka program akan menampilkan informasi terkait pasien

<img width="436" height="76" alt="image" src="https://github.com/user-attachments/assets/8382bcb4-0e71-4a74-8030-3d883396e1d1" />

sebaliknya jika kode unik tidak ditemukan pada daftar maka  program akan menampilkan bahwa pasien dengan kode tersebut tidak di temukan

<img width="446" height="98" alt="image" src="https://github.com/user-attachments/assets/58c226c0-24da-49f8-95e6-e31ccd0952ad" />

ketika user memasukkan angka 4 pada pilihan maka program akan meminta kode unik pasien yang ingin di hapus, selanjutnya program akan memberitahukan bahwa pasien dengan kode tersebut berhasil dihapus

<img width="466" height="55" alt="image" src="https://github.com/user-attachments/assets/914036c3-2d91-4fd4-85fe-f050093d29c7" />

sebaliknya jika user memasukkan kode pasien yang tidak terdapat pada daftar maka program akan menampilkan bahwa pasien dengan kode unik tersebut tidak tersedia

<img width="264" height="141" alt="image" src="https://github.com/user-attachments/assets/4fed10e3-8c6c-4eb2-9e11-12fd3aede5fa" />

ketika user memasukkan angka 5 maka program akan selesai dan menghentikan perulangan pada program
