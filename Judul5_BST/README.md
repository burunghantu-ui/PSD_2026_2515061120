# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana yang berguna untuk mengatur data nomor antrian pasien yang diberikan secara acak kepada psien karena suatu kesalahan teknis, dimana program ini dapat menyimpan nomor antrian, lalu untuk mengetahui nomor antrian setelah dan sebelum nomor antrian yang ingin di cari terdapat fitur yang dapat menampilkan nomor antrian terdekat setelah dan sebelum nomor antrian pasien yang di cari selain itu program ini juga dapat menghapus nomor antrian pasien yang telah dilayani dan fitur yang menampilkan sisa nomor pasien yang belum dilayani.

Program ini menggunakan metode pengelolaan data Binary Search Tree lanjut yang digunakan untuk bisa mengurutkan nomor pasien yang sebelumnya di berikan secara acak karena adanya kesalahan teknis tadi, selain itu dalam program ini menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada, selain itu perulangan for juga digunakan dalam mengecek sebanyak data pasien untuk menemukan nama pasien yang di cari. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

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

baris 31, terdapat percabangan dimana ketika node root itu kosong maka akan mengeksekusi baris 32 yang mana mengembalikan nilai none

baris 33, terdapat percabangan lain dengan kondisi dimana ketika key yang dimasukkan pengguna nanti lebih kecil dari pada nilai node root maka kana mengeksekusi baris 34 yang mana node root bagian kiri akan memanggil fungsi delete node.

baris 35 merupakan lanjutan dari percabangan di baris 33, dimana ketika key ternyata lebih besar di bandingkan nilai dalam node maka akan mengeksekusi baris 36 yang mana node kanan root akan kembali memanggil fungsi delete node

baris 37, terdapat kondisi ketika seluruh percabangan kondisi tidak terpenuhi maka akan mengeksekusi baris 38 yang terdapat percabangan lagi dengan kondisi dimana jika node root bagian kiri itu kosong dan node bagian kanan juga kosong maka akan mengeksekusi baris 39 yang mana akan mengembalikan nilai none

baris 40, terapat lanjutan dari percabangan di baris 37 dimana ketika node dari root kiri itu kosong maka akan mengekseksui baris 41 yang mana akan mengembalikan node root bagian kanan

baris 42, terdapat lanjutan percabangan dimana ketika node root bagian kanan itu kosong maka akan mengeksekusi baris 43 yang akan mengembalikan root kiri

baris 44, terdapat kondisi ketika seluruh percabangan kondisi tidak terpenuhi maka akan mengeksekusi baris 45-47

baris 45, terdapaat variabel successor yang mana akan memanggil fungsi find min node, lalu di baris 46, nilai root key akan diganti dengan nilai node successor tadi selanjutnya di baris 47 nide root bagian kanan akan memanggil fungsi delete node

baris 48, terdapat pengembalian nilai root

<img width="575" height="219" alt="image" src="https://github.com/user-attachments/assets/52954526-1c8b-4068-bc56-7fe1a493a777" />

baris 50, terdapat fungsi delete yang mana di dalamnya (baris 51) rootnya akan memanggil fungsi delete node

baris 53, terdapat fungsi height yang mencakup baris 54-58

baris 54, terdapat percabnagan dimana jika node root kosong maka akan mengembalika nilai -1 di 
baris 55

baris 56, terdapat variabel height left yang mana akan memanggil fungsi height kembali

baris 57, terdapat variabel height right yang mana akan memanggil fungsi height kembali

baris 58, terdapat pengembalian jumlah nilai 1 dengan memanggil nilai max yang didalamnya terdapat parameter berisi nilai height left dan height right

<img width="566" height="339" alt="image" src="https://github.com/user-attachments/assets/5f19678d-7339-4f28-98cb-32b5efa87b6e" />

baris 60, terdapat fungsi level order yang berguna untuk menampilkan nilai node dari Binary Tree, dimana fungsi ini mencakup baris 61-73

baris 61, terdapat percabangan dengan kondisi dimana ketika root bernilai none maka akan mengeksekusi baris 62-63 yang mana akan menampilkan 'kosong' lalu mengembalikan nilai fungsi

baris 64, terdapat list kosong queue

baris 65 merupakan penambahan nilau root ke data antrian 

baris 66 terdapat perulangan while, yang akan terus melakukan perulangan ekseskusi baris 67-72 selama panjang dari queue tidak lebih dari 0

baris 67 terdapat variabel sementara yang akan memamnggil nilai pop dari queue

baris 68 terdapat perintah menampilkan nilai dari node  current 

baris 69 terdapat percabangan kondisi dimana ketika node kiri current itu tidak bernilai kosong maka akan mengeksekusi baris 70 yang akan menambahkan nilai node kiri current kedalam queue

baris 71 adalah percabangan dengan kondisi dimana ketika node kanan current tidak bernilai kosong maka akan mengekseksusi baris 72 yang mana akan menambahkan nilai kanan current ke queue

baris 73, terdapat perintah menampilkan baris kosong agar tampilan selanjutnya tidak menyatu dengan tampilan dari fungsi level order ini

<img width="654" height="429" alt="image" src="https://github.com/user-attachments/assets/2aa4f8cd-bd36-4a29-b128-a369c65dbe13" />

baris 75, terdapat fungsi successor yang mana berfungsi untuk menemukan nilai yang tepat disamping dan lebih besar dari nilai yang dicari, fungsi ini mencakup baris 76-92

baris 76, terdapat variabel sementara current yang mana akan bernilai sama dengan root 

baris 77, terdapat variabel successor yang bernilai none 

baris 78 terdapat perulangan while yang akan terus melakukan perulangan ekseskusi dari baris 79-84 selama nilai current tidak kosong atau baris 85 di eksekusi

baris 79 terdapat percabangan dengan kondisi jika key lebih kecil dari nilai current maka akan mengeksekusi baris 80-81, dimana baris 80 terdapat variabel successor yang nilai nya akan disamakan dengan nilai current, dan di baris 81 nilai current akan diganti dengan nilai node kiri current

baris 82 terdapat percabangan lanjutan dari baris 79 dimana jika key ternyata lebih besar dari nilai current maka akan mengeksekusi baris 83 yang mana akan mengganti niali current menjadi node kanan current

baris 84, terdapat kondisi ketika seluruh percabangan kondisi tidak terpenuhi maka akan mengeksekusi baris 35 yang mana akan menghentikan perulangan

baris 86,, terdapa percabangan kondisi dimana ketika current itu none maka akan mengeksekusi baris 87 yang mana akan mengembalikan nilai none dan false

baris 88, terdapat percabangan dengan kondis jika nilai node current kanan itu tidak none maka akan mengeksekusi bari 89 dimana nilai successor akan memanggil fungsi find min mode dengan parameter nilai dari noe current kanan

baris 90, terdapat percabangan dengan kondisi ketika successor bernilai none maka akan mengeksekusi baris 91 yang mana akan mengembalikan nilai none dan false

baris 92, terdapat pengembalian nilai node successor dan boolean true

<img width="486" height="511" alt="image" src="https://github.com/user-attachments/assets/e440fb46-849b-41e0-9a2f-a8e339d9f970" />

baris 94, terdapat fungsi find predecessor yang berfungsi untuk menemukan nilai yang tepat lebih kecil dari nilai yang di cari atau nilai yyang berada tepat di belakang yang di cari, fungsi ini memuat baris 95-114

baris 95, terdapat variablecurrent yang akan mengimpan nilai node root

baris 96, terdapat variable predecessor yang mana saat ini bernilai none 

baris 97, terdapat perulangan while yang mana akan terus mengulang ekseskusi baris 108-103 selama nilai current tida none

baris 98, terdapat percabangan dengan kondisi ketika key lebih besar dari nilai current key maka akan mengeksekusi baris 99-100

baris 99, variabel predecessor akan bernilai sama seperti current lalu di baris 100 niali current akan diganti dengan currrent kanan.

baris 101, terdapat kondisi lanjutan dari baris 98 yang mana jika key ternyata lebih kecil dari nilai current maka akan mengeksekusi baris 102 yang akan mengganti nilai current saat itu dengan node kiri current

baris 103, terdapat kondisi ketika seluruh percabangan kondisi tidak terpenuhi maka akan mengeksekusi baris 104 yang mana akan menghentikan perulangan baris 97

baris 105 terdapat percabangan dengan kondisi ketika nilai current itu none maka akan menngeksekusi baris 106 yang mana akan mengembalikan nilai none dan booleann berupa false

baris 107, terdapat kondisi dimana ketika nilai node kiri itu tidak none maka akan mengeksekusi baris 108-111 yang mana di baris 108 terdapat variabel temp yang akan menyimpan nilai node kiri current

baris 109, terdapat perulangan yang mana ketika nilai node kanan dari tempt tidak none maka akan terus menngeksekusi baris 110 yang mana variabel tempt akan diganti dengan node kanan dari tempt

baris 111, nilai predecessor akan diganti dengan nilai tempt

baris 112, terdapat percabangan kondisi ketika predecessor bernilai none maka akan mengeksekusi baris baris 113 yang akan mengembalikan nilai none dan false

baris 114, terdapat pengembalian nilai predecessor dan true

<img width="777" height="153" alt="image" src="https://github.com/user-attachments/assets/bd4ab2a0-810d-47ab-9e13-77cbdaed40ae" />

baris 116, merupakan fungsi utama yang didalamnya terdapat logika utama program, fungsi ini mencakup baris 117-181

baris 117, terdapat variabel bst yang menampung class BSTLanjut

118, terdapat variabel pilih yang saat ini bernilai 0

baris 119-121 akan menampilkan judul dari program ini

<img width="1125" height="285" alt="image" src="https://github.com/user-attachments/assets/bd9dd5ba-f0b0-4bab-89fd-3e071e6fd798" />

baris 123, terdapat perulangan while yang akan terus mengulang baris 124-181 selama tidak terpicu kondisi break

baris 124-129 akan menampilkan daftar apa saja yang user bia lakukan dalam program

baris 130, terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel pilihan di baris 131 sesuai dengan yang diinginkan yaitu integer 

baris 132, terdapat exception ValueError yang akan dieksekusi ketika input user di baris 131 bukan integer dan mengeksekusi baris 133 yang menampilkan 'input tidak valid!' lalu kembali meminta user melakukan input ulang, di baris 134, merupakan pemicu untuk terus dilakukannya permintaan input berulang hingga input user berupa integer

<img width="655" height="175" alt="image" src="https://github.com/user-attachments/assets/788a7d94-3efc-4122-b768-b4f5a71de3b1" />

baris 135, merupakan kondisi dimana ketika pilih yang dimasukkan dengan user bernilai 1 maka akan mengekseksui baris 136-141

baris 136, terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel pilihan di baris 137 sesuai dengan yang diinginkan yaitu integer lalu di baris 138 akan memasukkan nilai x tersebut ke bst menggunakan fungsi insert, dan di baris 139 akan memapilkan bahwa nilai yang dimasukkan user berhasil di masukkan 

baris 140, terdapat exception ValueError yang akan dieksekusi ketika input user di baris 137 bukan integer dan mengeksekusi baris 141 yang menampilkan 'input tidak valid!'

<img width="976" height="241" alt="image" src="https://github.com/user-attachments/assets/bc08cec6-139c-4ad8-8d41-235b304ce251" />

baris 143, merupakan lanjutan kondisi baris 135 dimana ketika pilih user tenyata sama dengan 2 maka akan mengeksekusi baris 144-152

baris 144, terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel x di baris 145 sesuai dengan yang diinginkan yaitu integer lalu di baris 146 terdapat variabel ans dan found yang akan menampung pengembalian dari memanggil fungsi find successor dengan memasukkan root dari bst dan nilai x yang dimasukkan user sebelumnya

baris 147, terdapat percabangan dimana ketika found itu true maka akan mengekseskusi baris 148 yang mana akan menampilakn ans atau nilai successor, sebaliknya ketika found adalah false maka akan masuk ke percabangan baris 149 yang akan mengeksekusi baris 150 yan menampilkan bahwa successor tidak tersedia

baris 151, terdapat exception ValueError yang akan dieksekusi ketika input user di baris 145 bukan integer dan mengeksekusi baris 152 yang menampilkan 'input tidak valid!'

<img width="986" height="243" alt="image" src="https://github.com/user-attachments/assets/bf62a8a4-ba98-4d5e-8f15-4ded45fcc44d" />

baris 154, merupakan lanjutan kondisi baris 143 dimana ketika pilih user tenyata sama dengan 3 maka akan mengeksekusi baris 155-163

baris 155, terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel x di baris 156 sesuai dengan yang diinginkan yaitu integer lalu di baris 157 terdapat variabel ans dan found yang akan menampung pengembalian dari memanggil fungsi find successor dengan memasukkan root dari bst dan nilai x yang dimasukkan user sebelumnya

baris 162, terdapat exception ValueError yang akan dieksekusi ketika input user di baris 163 bukan integer dan mengeksekusi baris 163 yang menampilkan 'input tidak valid!'

<img width="579" height="178" alt="image" src="https://github.com/user-attachments/assets/9505b8b5-4b70-4fe1-90be-9dfb0662c7a8" />

baris 165, merupakan lanjutan kondisi baris 154 dimana ketika pilih user tenyata sama dengan 4 maka akan mengeksekusi baris 166-171

baris 166, terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel x di baris 167 sesuai dengan yang diinginkan yaitu integer lalu di baris 168 ada pemanggilan fungsi delete untuk menghapus nilai x dari Binary Tree, lalu do baris 169 akan menampilkan nilai yang diinginkan telah dihapus

baris 170, terdapat exception ValueError yang akan dieksekusi ketika input user di baris 171 bukan integer dan mengeksekusi baris 163 yang menampilkan 'input tidak valid!'

<img width="489" height="100" alt="image" src="https://github.com/user-attachments/assets/80361d7a-0b34-4f7f-a00d-6fb97202ed23" />

baris 173, merupakan lanjutan kondisi baris 165 dimana ketika pilih user tenyata sama dengan 5 maka akan mengeksekusi baris 174-176, dimana baris 174 akan menampilkan level order, dan di baris 175 akan terdapat pemanggilan fungsi level order lalu di baris 176 akan menampilkan baris kosong agar tampilan selanjutnya tidak tersambung dengan tampilan baris 174

<img width="503" height="130" alt="image" src="https://github.com/user-attachments/assets/ea48a36c-8556-428a-8d6e-7428cc968097" />

baris 178, merupakan lanjutan kondisi baris 165 dimana ketika pilih user tenyata sama dengan 6 maka akan mengeksekusi baris 179-180 dimana baris 179 akan menampilkan bahwa program selesai dan baris 180 akan mengakhiri perulangan baris 123

baris 181, merupakan lanjutan kondisi dimana ketika pilih user tenyata sama tidak bernilai 1-6 maka akan mengeksekusi baris 182 yang akan menampilkan bahwa pilihan tidak valid

<img width="328" height="52" alt="image" src="https://github.com/user-attachments/assets/897a1dac-5a4c-4c10-af8f-02e90b7b2025" />

baris 184-185 merupan pemanggilan dari fungsi utama 

# Output
<img width="820" height="228" alt="image" src="https://github.com/user-attachments/assets/4d87be91-6dbd-45af-9529-bb84d65b4de1" />

Output pertama yang ditampilakn program ketika pertama kali di jalankan sekaligus meminta input user

<img width="294" height="126" alt="image" src="https://github.com/user-attachments/assets/0a806824-c4a7-408a-bfc7-54a31330bcf6" />

ketika user mesaukkan angka  1 di pilhan maka akan diminta untuk memasukkan nomor antrian setelahnya program akan menampilkan bahwa nomor tersebut berhasil di simpan

<img width="241" height="120" alt="image" src="https://github.com/user-attachments/assets/515d8fd6-0ad2-42d5-a852-1734c88d928a" />

ketika user memilih untuk memasukkan pilihan 2 maka akan dimintai untuk  memasukkan nilai yang ingin di cek nomor setelahnya oleh user selanjutnya akan di tampilkan nilai tersebut

<img width="262" height="100" alt="image" src="https://github.com/user-attachments/assets/07a147d6-369d-41e8-bdb7-8470d80b5903" />

ketika user memasukkan angka 3 sebagai pilihan maka kan dimintai untuk  memasukkan nilai yang ingin di cek nomor sebelum angka yang di cari oleh user selanjutnya akan di tampilkan nilai tersebut

<img width="319" height="99" alt="image" src="https://github.com/user-attachments/assets/763723f8-b12d-420a-beb6-82cdcb1eefc0" />

ketika user memilih untuk memasukkan pilihan angka 4 maka akan dimintai untuk  memasukkan nilai yang ingin di hapus selanjutnya akan di tampilkan nilai tersebut telah terhapus dari binary tree

<img width="441" height="99" alt="image" src="https://github.com/user-attachments/assets/766db4db-aded-4223-88f4-8fd573fa559b" />

ketika user memilih untuk memasukkan pilihan angka 5 maka akan menampilkan level order atau menampilkan urutan binary tree dari atas ke bawah 

<img width="189" height="91" alt="image" src="https://github.com/user-attachments/assets/ad5002a4-1cc4-4ce4-87ba-3a5e229dc8bc" />

ketika user memilih untuk memasukkan pilihan angka  maka program akan selesai

<img width="287" height="79" alt="image" src="https://github.com/user-attachments/assets/14d52787-e663-4e0c-a374-e36390508c5c" />

ketika user memilih untuk memasukkan pilihan angka bukan dari 1-6 maka akan menampilkan bahwa pilihan tidak valid 

# Link Video YouTube

https://youtu.be/hkfmXP6FLHo
