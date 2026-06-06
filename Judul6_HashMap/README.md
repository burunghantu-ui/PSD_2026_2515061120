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

