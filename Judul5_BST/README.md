# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana yang berguna untuk mengatur data nomor antrian pasien yang diberikan secara acak kepada psien karena suatu kesalahan teknis, dimana program ini dapat menyimpan nomor antrian, lalu untuk mengetahui nomor antrian setelah dan sebelum nomor antrian yang ingin di cari terdapat fitur yang dapat menampilkan nomor antrian terdekat setelah dan sebelum nomor antrian pasien yang di cari selain itu program ini juga dapat menghapus nomor antrian pasien yang telah dilayani dan fitur yang menampilkan sisa nomor pasien yang belum dilayani.

Program ini menggunakan metode pengelolaan data Binary Search Tree lanjut yang digunakan untuk bisa mengurutkan nomor pasien yang sebelumnya di berikan secara acak karena adanya kesalahan tteknis tadi, selain itu dalam program ini menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada, selain itu perulangan for juga digunakan dalam mengecek sebanyak data pasien untuk menemukan nama pasien yang di cari. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

# Source Code
<img width="349" height="136" alt="image" src="https://github.com/user-attachments/assets/d220d80b-0aec-493d-9c0b-e1b74580bbdc" />

Baris 1 terdapat pendeklarasian kelas Node dimana di dalamnya terdapat fungsi (baris 2) yang digunakan untuk membuat suatu node sebelah kanan (baris 5) dari binary tree dan node kiri (baris 4) serat nilai kunci (baris 2)

<img width="706" height="503" alt="image" src="https://github.com/user-attachments/assets/3de4f3f5-2919-4b92-8949-c5d126218870" />

baris 8 terdapat kelas BST lanjut yang didalmnya memmuat fungsi fungsi yang dapat dilakukan oleh class tersebut 

baris 9 terdapat fungsi yang digunakan untuk membuat atau menyimpan node akar dari BST tadi (baris 10)

baris 12 terdapat fungsi insert noode yang memuat dari baris 13-19 yang mana di gunakan untuk memasukkan data ke dalam Binery tree (BT)

baris 13 terdapat percabangan dimana ketika akar saat itu bernilai none maka akam memanggil kelass node yang akan di isi dengan parameter key lalu akan di kembalikan (baris 14)

baris 15 terdapat percabangan dengan kondisi ketika key yang di itu lebih kecil dari nilai dari node akar atau root maka akan mengeksekusi baris 16 dimana nilai dari node root sebelah kiri akan diganti nilainya dengan key, dengan cara memanggil fungsi insert_node

baris 17 terdapat lanjutan percabangan baris 15, dengan kondisi ketika key lebih besar dari nilai dari node akar atau root maka akan mengeksekusi baris 18 dimana nilai dari node root sebelah kanan akan diganti nilainya dengan key, dengan cara memanggil fungsi insert_node

baris 19 merupakan pengembalian nilai node root

<img width="679" height="193" alt="image" src="https://github.com/user-attachments/assets/1df17a16-4a32-447e-affe-cbf95d25f2d1" />

baris 21, merupakan fungsi insert yang berfungsi memasukkan nilai root kedalam node (baris 22)

baris 24, merupakan fungsi  min node yang digunakan untuk menemukan nilai terkecil dalam node yang mana mencakup baris 25-28

baris 25, terdapat current sebagai variabel sementar yan akan menyimpan node root

baris 26, terdapat perulangan while dimana ketika node current bukan none dan node current sebelah kiri juga bukan none maka akan mengeksekusi baris 27 yang mana mengganti node current dengan node current sevelah kiri, selanjutnya di baris 28 nilai atau node current akan di kemablikan

<img width="762" height="453" alt="image" src="https://github.com/user-attachments/assets/9ac412cc-2591-44fd-9f0e-ece8159fda7a" />

baris 30, terdapat fungsi yang berguna untuk menghapus suatu node dimana mencakup baris 31-48

baris 31, 
