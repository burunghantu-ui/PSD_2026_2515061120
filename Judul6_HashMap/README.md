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

<img width="731" height="246" alt="image" src="https://github.com/user-attachments/assets/492e9e6b-8f20-4603-8998-d5dfccb24dfe" />

baris 65, terdapat fungsi display yang berguna untuk menampilkan keseluruhan daftar, dimana fungsi ini mencakup baris 66-74

baris 66, akan menampilkan "Isi Hash Table (Open Addressing, Linear Probing):"

baris 67, terdapat perulanagn for yang mencakup baris 68-74

baris 68, akan menampilkan urutan antrian pada daftar pasien atau table

baris 69, terdapat percabangan dengan kondisi dimana jika status data pada indeks ke i table sama dengan empty atau kosong maka akan mengekseskusi baris 70 yang mana akan menampilkan empty

baris 71, merupakan lanjutan percabangan sebelumnya dengan kondisi jika status data pada indeks ke i di daftar tabel sama dengan deleted atau telah dihapus sebelumya maka akan mengeksesuki baris 72 yang akan menampilkan "DELETED"

baris 73, merupakan lanjutan dari percabangan sebelumnya dimana jika tidak ada kondisi yang terpenuhi sebelumnya maka akan mengeksekusi baris 74 yang mana akan menampilkan key serta value data dari indeks ke i daftar table

