# Administrasi Klinik

## Deskripsi Singkat

Program ini merupakan program sederhana untuk mengetahui urutan pelayanan suatu pasien dengan mencari data melalui nama pasien tersebut, sekaligus mengetahui ada berapa banyak pasien yang memiliki nama yang sama.

Program ini menggunakkan sequential search untuk mengetahui urutan pasien berdasarkan indeks, dan mengetahui berapa banyak pasien dengan nama yang sama. Hal pertama yang dilakukan oleh sistem adalah menampilkan judul program diikuti dengan meminta user memasukkan jumlah pasien, selanjutnya program akan meminta user memasukkan data nama pasien sebanyak jumlah pasien lalu program akan meminta nama pasien yang ingin diketahui urutan dan banyaknya nama yang sama dengan nama tersebut, kemudian memberitahu berapa kali nama tersebut di temukan dalam program dan berada di urutan mana saja.

Menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada, selain itu perulangan for juga digunakan dalam mengecek sebanyak data pasien untuk menemukan nama pasien yang di cari. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

# Source Code

<img width="727" height="77" alt="image" src="https://github.com/user-attachments/assets/fb8227ca-484d-42fe-bf3c-1d64405d1093" />

Baris 1-3 di buat untuk mencetak judul program, serta garis pembatas untuk mempercantik.

<img width="477" height="211" alt="image" src="https://github.com/user-attachments/assets/2681ae99-0f83-4cf1-b1cb-6424cb6fbfc6" />

baris 5 terdapat fungsi search yang mencakup baris 6-13, dengan parameter berupa data pasien, jumlah pasien, target nama yang akan dicari, dan array indeks yang akan menampung indeks urut nama yang ditemukan

baris 6, terdapat variable count dengan value sementara 0 yang akan digunakan untuk menampung jumlah ditemukannya nama target

baris 7 terdapat variable i yang akan digunakan untuk menampung dan mengecek data atau urutan indeks pasien dengan nama tersebut

baris 8, terdapat perulangan while dimana akan mengulangi eksekusi baris 9-11 terus menerus selama nilai i tidak lebih besar atau sama dengan jumlah pasien

baris 9 terdapat percabangan if dengan kondisi dimana jika elemen pasien indeks ke i sama dengan target maka akan mengeksekusi baris 10-11 yang mana akan menambah value count sebanyak satu, dan menambahkan nilai i saat itu ke array indeks

baris 12, terdapat perintah dimana Ketika perulangan while saat itu selesai maka nilai i akan bertambah sebanyak 1 sebelum perulangan memeriksa apakah nilai sudah lebih besar sama dengan jumlah pasien sebelum melanjutkan ke perulangan selanjutnya, Ketika kondisi terpenuhi maka perulangan akan dilanjutkan.

baris 13 terdapat pengembalian nilai fungsi search Ketika akan dipanggil yaitu berupa variable count

<img width="622" height="220" alt="image" src="https://github.com/user-attachments/assets/86b4247d-85ee-442e-8922-2e6cb1538f70" />

baris 15 terdapat fungsi Utama yang mana mana memuat seluruh logika inti dalam program ini

baris 16 terdapat variable array pasien yang akan memuat yang akan memuat data nama pasien 

baris 17 terdapat array indeks yang akan berisi indeks atau nomor urut pasien dengan nama yang di cari

baris 18 terdapat perulangan while, yang digunakan untuk melakukan perulangan baris 19-23

baris 19 terdapat blok try yang akan memastikan input user di baris 20 sesuai yaitu berupa angka

baris 20 terdapat variable jml dimana akan akan meminta user memasukkan jumlah pasien yang nantinya akan disimpan ke variable jml

bari 21 adalah pengehentian perulangan di baris ke 18 dimana menandakan tidak perlu permintaan ulang untuk memasukkan nilai jml dikarenakan input sebelumnya telah sesuai

baris 22 terdapat blok except, dimana akan dieksekusi Ketika input jml bukan berupa integer sehingga menampilkan baris 23 dan Kembali mengeksekusi baris 20 untuk meminta ulang input, hal ini akan di lakukan hingga user memasukkan input berupa integer

<img width="846" height="221" alt="image" src="https://github.com/user-attachments/assets/1aed6a5b-7d3c-42d2-837d-db23750e0cd6" />

baris 24 terdapat perulangan for, dimana akan mengeksekusi baris 24-25 secara berulang sebanyak jml atau jumlah pasien, dimana baris 24 terdapat variable nama yang akan menyimpan nama sementara dari pasien yang akan di masukkan oleh user setelahnya nilai nama akan di tambahkan ke array pasien di baris 26

baris 27 terdapat permintaan input nama pasien yang akan dicari dan disimpan ke variable target

baris 28 terdapat variable count dimana akan bernilai berdasarkan nilai Kembali dari fungsi search, yaitu banyaknya nama yang dicari ditemukan

baris 29 terdapat percabangan if dengan kondisi jika nilai count leibih besar dari 0 maka akan mengeksekusi baris 30 yang akan menampilkan berapa kali nama yang di cari ditemukan di antrian, lalu di baris 31 terdapat perulangan for yang akan menampilkan seluruh elemen array indeks +1 untuk menghindari adanya antrian 0

baris 32 terdapat kelanjutan percabangan if di baris 29 dimana Ketika kondisi tidak terpenuhi maka akan mengeksekusi baris 32 yang akan mnampilkan pemberitahuan bahwa nama yang di cari tidak terdapat di antrian

<img width="151" height="36" alt="image" src="https://github.com/user-attachments/assets/8f32b0be-39c2-4472-95b9-3df922857925" />

baris 34 terdapat pemanggilan fungsi main di baris 15

# Output

<img width="566" height="137" alt="image" src="https://github.com/user-attachments/assets/ed5169f6-e8dd-4adc-8fc1-8eb3df071582" />

ketika program pertama kali dijalankan akan menampilkan judul program dari source code baris 1-3 dan meminta input jumlah pasien yang akan di akan di masukkan dalam antrian

setelahnya program akan meminta user memasukkan nama pasien sebanyak jumlah pasien yang telah di masukkan sebelumnya

<img width="417" height="202" alt="image" src="https://github.com/user-attachments/assets/ecca1784-348b-451e-acbb-5d15edeb0ceb" />

setelah user memasukkan seluruh nama pasien maka program akan menampilkan permintaan untuk memasukkan suatu nama yang ingin di cari dalam antrian

<img width="440" height="50" alt="image" src="https://github.com/user-attachments/assets/6f5bd6d7-c7e0-4ef8-9788-749846968019" />

selanjutnya program akan menampilkan berapa kali nama yang di cari dalam antrian di temukan dan berada di urutan mana saja

Ketika saat user memasukkan jumlah pasien tidak berupa integer maka program akan menampilkan perintah 'masukkan angka!' dan Kembali meminta input jumlah pasien

# Link YouTube


