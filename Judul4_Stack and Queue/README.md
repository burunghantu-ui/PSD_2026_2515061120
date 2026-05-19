# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program singkat yang mengatur administrasi klinik dengan mendata antrian pelayanan rumah sakit, dimana program ini dapat menambahkan pasien ke antrian, dan ketika pasien telah dilayani maka nama pasien tersebut akan dipindahkan ke dalam riwayat antrian pasien, karena terdapat kemungkinan terjadi kesalahan teknis dimana admin terburu buru memasukkan nama pasien yang tidak sengaja melewatkan gilirannya untuk dilayani ke dalam riwayat antrian pasien, maka disediakan fitur 'undo' untuk mengeluarkan nama pasien dari riwayat dan otomatis menempatkan pasien ke antrian terakhir, mengingat arsip riwayat antrian yang harus di perbarui tiap harinya maka dibuat fitur 'clear all' untuk mengosongkan riwayat pasien lama dan menggantinya dengan yang baru pada hari itu.

Program ini menggunakan metode pengelolaan data queue untuk antrian pasien dan stack untuk menampung riwayat pasien, dimana kedua metode ini menggunakan struktur data linked list atau linked list circular khusus untuk antrian. Hal pertama yang dilakukan oleh sistem adalah menampilkan judul program diikuti dengan menu daftar yang bisa dilakukan user seperti pengelolaan antrian, riwayat pasien, melihat seluruh antrian dan riwayat pasien saat itu. untuk pengelolaan antrian user dapat menambahkan nama pasien, memasukkan pasien terdepan yang telah di layani ke riwayat pasien dan melihat antrian saat ini, sedangkan pada pengelolaan riwayat pasien, user dapat mlihat riwayat, mengundo pasien terakhir yang dimasukkan ke antrian, dan membersihkan riwayat pasien hari itu.

Menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada, selain itu perulangan for juga digunakan dalam mengecek sebanyak data pasien untuk menemukan nama pasien yang di cari. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.
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

<img width="498" height="222" alt="image" src="https://github.com/user-attachments/assets/c6c3e329-4462-461f-b362-f6ff909ba053" />

baris 23, terdapat fungsi hapus yang mencakup baris 24-31, yang mana funngsi ini akan di gunakan untuk menghilangkan elemen terdepan dari antrian

baris 24, terdapat percabangan dengan kondisi ketika variabel yang dimaksud tenyata kosong maka akan menngeksekui baris 25 yang akan menampilkan bahwa antrian (queue) kosong, yang man hal ini akan dikembalikan dengan return di baris 26.

baris 27, terdapat variabel temp yang akan menyimpan sementara node terdepan yang akan di hapus

setelah menyimpan data tersebut maka node terdepan antrian akan di ganti dengan node setelahnya di baris 28.

baris 29, terdapat percabangan di mana ketika elemen data terdepan bernilai none stelah di geser di baris 28 maka akan mengeksekui baris 30, dimana mengubah elemen paling belakang dari antrian menjadi none.

baris 31 merupakan perintah pengembalian nilai elemen yyang tersimpan pada variabel temp pada saat itu

<img width="469" height="248" alt="image" src="https://github.com/user-attachments/assets/4f6176d7-2d36-40c9-9ab5-dc6fb9403cfc" />

baris 33 terdapat deklarasi fungsi display yang digunakan untuk menampilkan seluruh elemen dalam antrian, fungsi ini mencakup baris 34-42

baris 34, terdapat percabangan dengan kondisi jika antrian bernilai kosong (dengan memanggi fungsi is_empty) maka akan mengeksekusi baris 35,  yang akan menampilkan bahwa antrian (queue) kosong, yang man hal ini akan dikembalikan dengan return di baris 36.

baris 37, terdapat perintah untuk menampilkan "Antrian: "

baris 38 terdapaat variabel current yang digunakan untuk menyimpan sementara node terdepan dalam antrian .

baris 39, terdapat perulangan while yang akan terus mengeksekusi baris 40-41 selama node current tidak kosong.

baris 40 akan menampilkan nilai elemen dari node current saat itu selanjutnya di baris 41 node current akan diganti mmenjadi node selanjutnya dari node current saat itu

baris 42, digunakan agar tampilan kalimat tidak bersambung dengan tampilan selanjutnya.

<img width="371" height="76" alt="image" src="https://github.com/user-attachments/assets/8d736444-ca2c-42c3-85c5-3ac5b268cc97" />

baris 44, terdapat deklarasi kelas riwayat pasien yang akan menyimpan data riwayat pasien yang telah di layani, dimana dalam kelas ini terdapat berbagai fungsi yang dapat di gunakan pada data riwayat antrian tersebut.

baris 45, terdapat fungsi init yang di dalamnya yaitu baris 46 terdapat pendeklarasian bahwa data teratas saat itu memiliki none node

<img width="418" height="57" alt="image" src="https://github.com/user-attachments/assets/f0aad16a-6f5d-446d-a68b-6454013bf137" />

baris 48, terdapat fungsi is_empty dimana dibaris 49 dia akan mengembalikan nilai bahwa node teratas itu none, ketika node teratas saat itu memang none

<img width="543" height="166" alt="image" src="https://github.com/user-attachments/assets/28a617fa-a404-40ed-ade2-d9c82a85fb5e" />

baris 51, terdapat fungsi pop yang mencakup baris 52-57, fungsi ini berfunngsi untuk menghiilangkan node atau nilai node teratas dari data

baris 52, terdapat percabangan dengan kondisi jika antrian bernilai kosong (dengan memanggi fungsi is_empty) maka akan mengeksekusi baris 53,  yang akan menampilkan bahwa antrian (queue) kosong, yang man hal ini akan dikembalikan dengan return di baris 54.

baris 55, terdapat variabel temp yang akan menyimpan sementara node teratas yang akan di hapus

setelah menyimpan data tersebut maka node teratas riwayat akan di ganti dengan node teratas selanjutnya di baris 56.

baris 57 merupakan perintah pengembalian nilai elemen yang tersimpan pada variabel temp pada saat itu 

<img width="426" height="99" alt="image" src="https://github.com/user-attachments/assets/e96fe8f4-c167-4ed0-9628-9be2ab37f117" />

baris 59, terdapat fungsi push yang mencakup baris 60-62, dimana fungsi ini berguna untuk menambahkan elemen ke dalam riwayat

baris 60 terdapat variabel new node yang mana memnaggil kelas Node yang sebagai node baru yang bervalue x

baris 61, node selanjutnya dari new_node akan berubah menjadi node teratas dalam riwayat

baris 62, akan menukar atau menggeser node baru (new_node) menjadi menjadi node teratas dalam riwayat

<img width="441" height="78" alt="image" src="https://github.com/user-attachments/assets/68c8152d-ad2c-409c-8e0d-99ae91a7c652" />

baris 64, terdapat fungsi clear yang mencakup baris 65-66, dimana fungsi ini berguna untuk mengosongkan data riwayat, cara kerja fungsi ini ada di baris 65, dimana node teratas akan di ubah menjadi none atau tidak terdapat elemen selanjutnya akan di tampilkan baris 66 yang berisi 'stack di kosongkan!'

<img width="743" height="242" alt="image" src="https://github.com/user-attachments/assets/2d80af76-996d-447b-a92e-fdcda2501287" />

baris 68 terdapat deklarasi fungsi display yang digunakan untuk menampilkan seluruh elemen dalam riwayat, fungsi ini mencakup baris 69-77

baris 69, terdapat percabangan dengan kondisi jika antrian bernilai kosong (dengan memanggi fungsi is_empty) maka akan mengeksekusi baris 70,  yang akan menampilkan bahwa antrian (stack) kosong, yang mana hal ini akan dikembalikan dengan return di baris 71.

baris 72, terdapat perintah untuk menmapilkan "Isi riwayat (atas ke bawah): "

baris 73 terdapaat variabel current yang digunakan untuk menyimpan sementara node teratas dalam riwayat.

baris 74, terdapat perulangan while yang akan terus mengeksekusi baris 75-76 selama node current tidak kosong.

baris 75 akan menampilkan nilai elemen dari node current saat itu selanjutnya di baris 76 node current akan diganti mmenjadi node selanjutnya dari node current saat itu

baris 77, digunakan agar tampilan kalimat tidak bersambung dengan tampilan selanjutnya.

<img width="490" height="125" alt="image" src="https://github.com/user-attachments/assets/5cabb946-3861-4d23-805a-c004b1a2ba3c" />

baris 79-83, terdapat fungsi menu yang berisi daftar pilihan yang bisa di lakukan dalam program

<img width="533" height="124" alt="image" src="https://github.com/user-attachments/assets/70844ddf-1b82-44a4-b587-847fb87db579" />

baris 85-89 terdapat menuantri yang berisi daftar apa saja yang bisa dilakukan pada antrian

<img width="404" height="124" alt="image" src="https://github.com/user-attachments/assets/d5a74179-3283-49ff-8921-03e33c97451b" />

baris 91-95 terdapat fungsi riwayat antrian dimana berisi daftar pilihan yang bisa di lakukan pada riwayat antrian pasien

<img width="779" height="153" alt="image" src="https://github.com/user-attachments/assets/5219dad5-6874-40e4-b9bb-8d3ec47569f5" />

baris 97, terdapat fungsi utama yang mmenjalankan logika utama dari program ini

baris 98 terdapat variabel antri yang menyimpan nilai, node dan keseluruhan dari kelas Antrian pada baris 6

baris 99 terdapat variabel riwayat yang menyimpan nilai, node dan keseluruhan dari kelas riwayatpasien pada baris 44

baris 100-102 berfungsi untuk menampilkan judul program ketika program pertama kali di jalankan 

<img width="537" height="201" alt="image" src="https://github.com/user-attachments/assets/2c07acde-f297-44aa-8c37-c19a4d03a7df" />

baris 104, terdapat perulangan while yang akan terus mengulang baris 105-162, yang mana hanya akan berhenti ketika suatu kondisi terpenuhi dan memicu break, dimana baris 105 terdapat pemanggilan fungsi menu yaitu daftra pilihan yang bisa di jalan kan oleh program

baris 106, terdapat perulangan while yang akan terus mengulang baris 107-132, yang mana hanya akan berhenti ketika suatu kondisi terpenuhi dan memicu break

baris 107 terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel pilihan di baris 108 sesuai dengan yang diinginkan yaitu integer lalu memicu baris 109 untuk menghentikan perulangan yang disebabkan jika user memasukkan sebaliknya, lalu melanjutkan ke kode baris selanjutnya

baris 110 terdapat exception ValueError yang akan dieksekusi ketika input user di baris 108 bukan integer dan mengeksekusi baris 111 yang menampilkan 'input tidak valid!' lalu kembali meminta user melakukan input ulang, hal ini akan terus dilakukan berulang hingga input user berupa integer

<img width="550" height="189" alt="image" src="https://github.com/user-attachments/assets/384bcd23-a10f-4646-a08c-ca33ac136e0b" />

baris 112 terdapat percabangan pengondisian dimana ketika inpu user di baris 108 sama dengan 1 maka akan mengeksekusi baris 113-132

baris 113, terdapat perulangan while yang akan terus mengulang baris 114-132, yang mana hanya akan berhenti ketika suatu kondisi terpenuhi dan memicu break

baris 114 terdapat pemanggilan menu antri yang akan menampilkan menu pilihan

baris 115 terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel pilih di baris 116 sesuai dengan yang diinginkan yaitu integer lalu melanjutkan ke kode baris selanjutnya

baris 117 terdapat exception ValueError yang akan dieksekusi ketika input user di baris 116 bukan integer dan mengeksekusi baris 118 yang menampilkan 'input tidak valid!' lalu kembali meminta user melakukan input ulang, di baris 119, merupakan pemicu untuk terus dilakukannya permintaan input berulang hingga input user berupa integer

<img width="652" height="316" alt="image" src="https://github.com/user-attachments/assets/209d50ce-95ee-495a-93e1-13343cea0c17" />

baris 120, terdapat percabangan kembali dimana ketika input user di baris 116 sama dengan 1 maka akan mengeksekusi baris 121-122, dimana baris 121 akan meminta user memasukkan nama pasien lalu dimasukkan ke dalam antrian dengan menggunakan fungsi tambah di baris 122

baris 123 merupakan kelanjutan dari baris 120 dimana ketika kondisi sebelumnya tidak terpenuhi dan input user ternyata sama dengan 2 maka akan mengeksekusi baris 124-126, dimana pada baris 124 terdapat variabel yang akan menyimpan elemen terdepan sementara dengan menggunakan fungsi hapus, lalu pada baris 125 nilai elemen ini akan di masukkan ke dalam riwayat dengan menggunakan fungsi push. lalu baris 126 akan memeberi tahu pasien dengan antrian terdepan telah di layani

<img width="353" height="52" alt="image" src="https://github.com/user-attachments/assets/013556e6-c277-4aea-a502-3cba874ef573" />

baris 127 terdapat lanjutan percabanga 120 dimana ketika input user di baris 116 sama dengan 3 maka akan mengeksekusi baris 128 yang mana akan menampilkan seluruh elemen dalam antrian dengan menggunakan fungsi display

<img width="501" height="108" alt="image" src="https://github.com/user-attachments/assets/6d0b37e1-4c76-42cf-86b8-67270e536af6" />

baris 129, merupan kondisi dimana ketika input user pada baris 116 sama dengan 4 maka akan mengeksekusi baris 130 yang terdaoat break dimana akan menghentikkan perulangan while di baris 113

baris 131 merupakan kondisi alternatif ketika input user baris 116 tidak memenuhi seluruh kondisi sebelumnya maka akan di eksekusi baris 132 yang menampilkan "input tidak valid!" lalu kembali mengeksekusi baris 114-132.

<img width="508" height="194" alt="image" src="https://github.com/user-attachments/assets/cb62639b-7e7e-4348-ac34-b8ed1b244a0e" />

baris 134 merupakan lanjutan percabangan di baris 112, yang mana ketika inout user di baris 108 sama dengan 2 maka baris 135-153 akan dieksekusi

baris 135, terdapat perulangan while yang akan terus mengulang baris 136-153, yang mana hanya akan berhenti ketika suatu kondisi terpenuhi dan memicu break

baris 136 terdapat pemanggilan menu riwayatantrian yang akan menampilkan menu pilihan

baris 137 terdapat exception handling yang mana digunakan untuk memastikan tipe data input user ke variabel pilih di baris 138 sesuai dengan yang diinginkan yaitu integer lalu melanjutkan ke kode baris selanjutnya

baris 139 terdapat exception ValueError yang akan dieksekusi ketika input user di baris 138 bukan integer dan mengeksekusi baris 140 yang menampilkan 'input tidak valid!' lalu kembali meminta user melakukan input ulang, di baris 141, merupakan pemicu untuk terus dilakukannya permintaan input berulang hingga input user berupa integer

<img width="732" height="148" alt="image" src="https://github.com/user-attachments/assets/2ea94bc6-e4ab-4d03-ac94-83fa848a8b00" />

baris 142 terdapat percabangan dengan kondisi jika input user di baris 138 sama dengan 1 maka baris 143 akan dieksekusi yaitu menampilkan seluruh elemen riwayat menggunakan fungsi display

baris 144 terdapat kelanjutan kondisi percabangan baris 142 yang mana ketika input user di baris 138 sama dengan 2 maka akan mengeksekusi baris 145-147, dimana pada baris 145 terdapat variabel yang akan menyimpan elemen teratas sementara dengan menggunakan fungsi pop, lalu pada baris 146, nilai elemen ini akan di masukkan ke dalam riwayat dengan menggunakan fungsi tambah. lalu baris 147 akan memeberi tahu "riwayat pasien {b} berhasil di batalkan"

<img width="526" height="155" alt="image" src="https://github.com/user-attachments/assets/12c66863-5c2c-4857-ae40-30e154d7823f" />

baris 148, merupakan lanjutan kondisi dimana ketika input user di baris 138 sama dengan 3 maka akan mengeksekusi baris 149 yang mana akan mengosongkan riwayat pasien menggunakan fungsi clear

baris 150 terdapat lanjutan kondisi kembali dimana ketika input user dibaris 138 sama dengan 4 maka akan mengeksekusi baris 151 yang terdapat break dimana akan menghentikkan perulangan while di baris 135

baris 152 merupakan kondisi alternatif ketika input user baris 138 tidak memenuhi seluruh kondisi sebelumnya maka akan di eksekusi baris 153 yang menampilkan "input tidak valid!" lalu kembali mengeksekusi baris 136-153.

<img width="365" height="74" alt="image" src="https://github.com/user-attachments/assets/3079a7f8-6293-4717-af0c-e9c2cc38f981" />

baris 155 merupakan lanjutan percabangan baris 112, dimana ketika input user di baris 108 sama dengan 3 maka baris 156-157 akan dieksekusi dimana baris 156 akan menampilkan seluruh elemen antri saat ini menggunakan fungsi display dan baris 157 akan menampilkan seluruh elemen riwayat saat ini menggunakan fungsi display

<img width="451" height="97" alt="image" src="https://github.com/user-attachments/assets/bf54207e-62a6-4efc-879f-af7622cdb3b0" />

baris 159 terdapat lanjutan kondisi dimana ketika input user di baris 108 sama dengan 4 maka maka akan mengeksekusi baris 160 yang terdapat break dimana akan menghentikkan perulangan while di baris 104

baris 161 merupakan kondisi alternatif ketika input user baris 108 tidak memenuhi seluruh kondisi sebelumnya maka akan di eksekusi baris 162 yang menampilkan "input tidak valid!" lalu kembali mengeksekusi baris 105-162.

<img width="133" height="32" alt="image" src="https://github.com/user-attachments/assets/3330be28-5f04-4246-b354-026085d6cc38" />

baris 164 terdapat pemanggilan fungsi menu yang merupakan logika utama program

# Output
<img width="543" height="206" alt="image" src="https://github.com/user-attachments/assets/92a9e2ac-a818-4649-aeb4-e35c97044289" />

output pertama yang di tampilkan oleh program ini adalah judul program yang mana berasal dari baris 100-102, dan menu utama yang di dalamnya terdapat bagian antrian dan riwayat

<img width="339" height="118" alt="image" src="https://github.com/user-attachments/assets/2c2428f6-cd2f-4614-94f3-6561d44dec9a" />

ketika memilih pilihan 1 dan memasukkan input 1 maka user akan masuk ke program antrian dan akan memberi tampilan menu yang ada dalam antrian berikutnya yang dapat dipilih oleh user 

<img width="386" height="137" alt="image" src="https://github.com/user-attachments/assets/4789b5d4-b3e2-4ba8-8fb2-85772a94597f" />

pada menu ini ketika user memilih nomor 1 maka program akan meminta user untuk memasukkan nama pasien untuk di tambahkan ke antrian dan akan kembali menampilkan menu dan permintaan inout yang sama

<img width="357" height="145" alt="image" src="https://github.com/user-attachments/assets/0ac52a39-4b73-4352-a442-31ff3b5615e8" />

ketika user memasukkan input angka 2 maka pasien yang berada di barisan terepan akan dilayani dan otomatis akan di masukkan ke riwayat antrian pasien 

<img width="337" height="139" alt="image" src="https://github.com/user-attachments/assets/7ece0358-674b-4cce-9266-6dc4828d88b3" />

ketika user memasukkan angka 3 maka akan menampilkan antrian saat itu

<img width="290" height="183" alt="image" src="https://github.com/user-attachments/assets/37be9721-6888-4ee0-8b37-dc482a3f35d4" />

ketika user memasukkan angka 4 maka program akan keluar dari perulangan program antrian dan kembali ke tampilan menu awal dan meminta user unntuk memilih menu kembali

<img width="273" height="201" alt="image" src="https://github.com/user-attachments/assets/0ce39832-2041-4e70-b7ee-f3b38c6830d0" />

dan ketika user memasukkan angka 2 pada menu ini maka user akan dialihkan ke program antrian pasien, dimana juga akan menampilkan menu yang bisa dipilih oleh user terkait ariwayt tersebut

<img width="494" height="154" alt="image" src="https://github.com/user-attachments/assets/e17e89a8-9348-4e94-b80f-e1734f9d4da6" />

dalam program riwayat ketika user memilih nomor 1 maka akan diperlihatkan riwayat antrian pasien pada saat itu, lalu kembali meminta user untuk memilih aksi selanjutnya 

<img width="388" height="141" alt="image" src="https://github.com/user-attachments/assets/80a0b707-e161-4463-a16a-c18379332707" />

lalu ketika user memilih nomor 2 maka riwayat antrian terakhir akan di batalkan dan dikembalikan ke antrian paling belakang

<img width="213" height="150" alt="image" src="https://github.com/user-attachments/assets/65bafd9d-0705-4ade-a98f-9efeb8b0f66f" />

ketika user memilih nomor 3 maka riwayat pasien pada saat itu akan di kosongkan 

<img width="290" height="185" alt="image" src="https://github.com/user-attachments/assets/71b561e8-44b6-43b0-b544-738f4f003d61" />

ketika user memilih no 4 maka program riwayat akan di hentikan dan user akan di kembalikan ke program atau menu awal, dan meminta input menu utama kembali kepada user

<img width="300" height="164" alt="image" src="https://github.com/user-attachments/assets/abd6332c-e299-4493-87f5-587b2b329176" />

pada menu utama ketika user memilih nomor 3 maka akan menampilkan seluruh antrian saat itu serta riwayat antrian pasien pada saat itu

<img width="480" height="135" alt="image" src="https://github.com/user-attachments/assets/ce2da89c-9cf7-41d4-a04c-8bb505e3fa6d" />

ketika user memilih angka 4 maka program utama akan selsesai 

<img width="316" height="279" alt="image" src="https://github.com/user-attachments/assets/edae2bb9-cfe8-4a21-8839-dd1155ce3ab2" />

ketika input yang dimasukkan user melebihi atau tidak didalam pilihan yang tersedia maka akan menampilkan pemberitahuan bahwa output tidak valid dan kembali menampilkan menu dan permintaan input ulang

<img width="264" height="153" alt="image" src="https://github.com/user-attachments/assets/9132e1b2-4c03-4d6a-bbe7-e84a7ff91020" />

dan ketika user memasukkan input selain angka maka akan menampilkan pemberitahuan bahwa input tidak valid dan meminta ulang masukkan input kepada user

# Link YouTube
https://youtu.be/u4FteML_Dwo
