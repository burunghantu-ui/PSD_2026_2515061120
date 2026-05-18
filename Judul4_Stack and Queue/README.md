# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program singkat yang mengatur administrasi klinik dengan mendata antrian pelayanan rumah sakit, dimana program ini dapat menambahkan pasien ke antrian, dan ketika pasien telah dilayani maka nama pasien tersebut akan dipindahkan ke dalam riwayat antrian pasien, karena terdapat kemungkinan terjadi kesalahan teknis dimana admin terburu buru memasukkan nama pasien yang tidak sengaja melewatkan gilirannya untuk dilayani ke dalam riwayat antrian pasien, maka disediakan fitur 'undo' untuk mengeluarkan nama pasien dari riwayat dan otomatis menempatkan pasien ke antrian terakhir, mengingat arsip riwayat antrian yang harus di perbarui tiap harinya maka dibuat fitur 'clear all' untuk mengosongkan riwayat pasien lama dan menggantinya dengan yang baru pada hari itu.
# Source Code
<img width="380" height="102" alt="image" src="https://github.com/user-attachments/assets/fd7276d6-fdd8-4cb0-9cad-206df53f1368" />

baris 1 terdapat deklarasi class Node 

baris 2 terdapat deklarasi fungsi init yang akan otomatis dipanggil ketika sebuah objek Node dibuat.

baris 3, terdapat atribut data dari objek (self.data) diisi dengan nilai dari parameter data

baris 4, terdapat atribut next dari objek (self.next) diinisialisasi dengan nilai None. Atribut ini berfungsi sebagai penunjuk (pointer) ke node berikutnya dalam linked list. 

<img width="350" height="101" alt="image" src="https://github.com/user-attachments/assets/821a5dc2-65bc-4c48-87cb-8a7836e8aadd" />

baros 6,, terdapat class antrian yang didalamnya terdapat fungsi fungs yang dapat digunakan ketika kelas antrian dipanggil

baris 7, terdapat fungsi init yang didalmnya terdapat pendaklarasian di baris 8, bahwa data terdepan antrian bernilai none, dan dibaris 9, mendeklarasikan data paling atas atau paling belakang saat itu juga bernilai none

<img width="440" height="56" alt="image" src="https://github.com/user-attachments/assets/27b02adf-4493-45da-87a5-a027aa04d04b" />

baris 11, terdapat pendeklarasian fungsi i_empty, dimana di baris 12 terdapat pengembalian nilai ketika data antrian itu bernilai none

<img width="492" height="196" alt="image" src="https://github.com/user-attachments/assets/56611ac6-0bcd-4ece-bfb1-1ab0b380cdd4" />

baris 14, terdapat fungsi tambah yang mencakup baris 15 sampai 21, fungsi ini sendiri berguna untuk menambahkan nilai ke variabel linked list

baris 15, terdapat variabel new node yang nilainya memanggi kelas Node dengan paraeter x, sehingga new node akan bernilai self data yang bervalue x

baris 16, terdapat percabangan if dimana ketika data itu kosong, yang mana hal ini di ketahui dengan memanggil funngsi is_empty, maka akan mengeksekusi baris 17-18.

baris 17, terdapat pergantian value terdepan antrian dengan value new_node. dan di baris 18 juga terdapat pergantian value antrian paling belakang dengan value new_node.

baris 19, merupakan kelanjutan dari baris 17, dimana ketika kondisi baris 17 tidak terpenuhi maka akan mengekseskui baris 20-21

baris 20, merupakan pergantian value index selanjutanya dari antrian paling belakang dengan value new_node, dan baris 21 merupakan pergantian value antrian paling belakang dengan value new node juga

<img width="514" height="219" alt="image" src="https://github.com/user-attachments/assets/5dff184d-8043-4fc8-af27-a563bee2e42b" />

baris 23, terdapat fungsi hapus yang mencakup baris 24-31, yang mana funngsi ini akan di gunakan untuk menghilangkan elemen terdepan dari antrian

baris 24, terdapat percabangan dengan kondisi ketika variabel yang dimaksud tenyata kosong maka akan menngeksekui baris 25 yang akan menampilkan bahwa antrian (queue) kosong, yang man hal ini akan dikembalikan dengan return di baris 26.

baris 27, terdapat variabel temp yang akan menyimpan sementara node terdepan yang akan di hapus

setelah menyimpan data tersebut maka node terdepan antrian akan di ganti dengan node setelahnya di baris 28.

baris 29, terdapat percabangan di mana ketika elemen data terdepan bernilai none stelah di geser di baris 28 maka akan mengeksekui baris 30, dimana mengubah elemen paling belakang dari antrian menjadi none.

baris 31 merupakan perintah pengembalian nilai elemen yyang tersimpan pada variabel temp pada saat itu

<img width="599" height="240" alt="image" src="https://github.com/user-attachments/assets/4cf4f62d-fa19-431c-a9d1-f5a24b816e3c" />

baris 33 terdapat deklarasi fungsi display yang digunakan untuk menampilkan seluruh elemen dalam antrian, fungsi ini mencakup baris 34-42

baris 34, terdapat percabangan dengan kondisi jika antrian bernilai kosong (dengan memanggi fungsi is_empty) maka akan mengeksekusi baris 35,  yang akan menampilkan bahwa antrian (queue) kosong, yang man hal ini akan dikembalikan dengan return di baris 36.

baris 37, terdapat perintah untuk menmapilkan "Isi queue (depan ke belakang): "

baris 38 terdapaat variabel current yang digunakan untuk menyimpan sementara node terdepan dalam antrian .

baris 39, terdapat perulangan while yang akan terus mengeksekusi baris 40-41 selama node current tidak kosong.

baris 40 akan menampilkan nilai elemen dari node current saat itu selanjutnya di baris 41 node current akan diganti mmenjadi node selanjutnya dari node current saat itu

baris 42, digunakan agar tampilan kalimat tidak bersambung dengan tampilan selanjutnya.

<img width="371" height="76" alt="image" src="https://github.com/user-attachments/assets/8d736444-ca2c-42c3-85c5-3ac5b268cc97" />

baris 44, terdapat deklarasi kelas riwayat pasien yang akan menyimpan data riwayat pasien yang telah di layani, dimana dalam kelas ini terdapat berbagai fungsi yang dapat di gunakan pada data riwayat antrian tersebut.

baris 45
