# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana untuk mendata pasien berdasarkan umur untuk ditentukannya antrian pelayanan, dimana pasien di bawah 50 tahun dan lansia di atas 60 tahun akan di prioritaskan berdasarkan seberapa jauh jarak umur dari batasan yang telah ditetapkan tersebut, jika ada kesamaan jarak umur pasien dari ketentuan maka akan diurutkan berdasarkan urutan input, sedangkan pasien umur 50-60 akan ditempatkan diakhir dan diurutkann sesuai urutan angka dari terbesar yaitu 60-50.

Program ini menggunkan metode sorting selection yang menggunakan elemen acuan sebagai pembanding dengan elemen lain, sehingga cocok dengan kebutuhan program. hal pertama yang akan ditampilkan dari program ini adalah judul program diikuti dengan meminta user memasukkan jumlah pasien lalu meminta umur pasien sebanyak jumlah pasien menggunakan perulangan for, lalu data tersebut akan diurutkan dalam fungsi selection sort, pada program ini saya memisahkan data menjadi 2 array, dimana yang satu elemennya bernilai tidak lebih dari 49 dan lebih besar dari 60, lalu yang lainnya berisi angka 50-60 sehingga umur 50-60 dapat saya tempatkan diakhir antrian.

Menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga dapat memanggil blok exception dan bisa di tampilkan secara berulang ulang sampai input yang user masukkan sesuai, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada. Program ini menggunakan percabangan if yang dimana digunakan untuk menentukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

# Source Code
<img width="677" height="86" alt="image" src="https://github.com/user-attachments/assets/07106aba-c5af-473d-8059-05b34eb949a7" />


Baris 1-3 di buat untuk mencetak judul program, serta garis pembatas untuk mempercantik.

<img width="355" height="104" alt="image" src="https://github.com/user-attachments/assets/d34a55f9-8f7c-4c0c-aeb4-6500eb0168c0" />


baris 5-8 merupakan fungsi tukar, dimana baris 5 merupakan deklarasi dari nama fungsu tersebut berfungsi menukar posisi elemen pada suatu array.

baris 6 memiliki variabel 'temp' yang berfungsi sebgai tempat menyimpan nilai sementara array arr indeks ke i

baris 7 merupakan fungsi dimana nilai elemen arr indeks i akan di isi nilai oleh arr indeks ke j

dan baris 8 dimana arr indeks ke j elemennya akan di isi oleh nilai variabel temp yang sebelumya memuat nilai arr indeks ke i

<img width="980" height="247" alt="image" src="https://github.com/user-attachments/assets/21bfb250-67cd-441a-b8cd-cf8625b273fd" />


dibaris 11-20 terdapat fungsi selection sort dengan parameter array, jumlah pasien, dan array angka 50-60, dimana baris satu sebagai deklarasi fungsi tersebut

baris 12 terdapat variabel n dimana memiliki value dimana jumlah pasien dikurangi dengan jumlah array m yang berisi angka 50-60 sesuai dengan input user

baris 13 terdapat perulangan for yang akan mengulang baris 14-18, dimana akan berulang sebanyak n-1 kali, hal ini dilakukan mengingat perulangan selalu dimulai dari 0, selain itu hal ini dilakukan untuk mencegah perulangan ini mencapai elemen terakhir untuk melakukan perbandingan, sehingga elemen terakhir hany akan bisa di akses oleh perulangan for selanjutnya

baris 14, dimana setiao kali perulangan baris 13 dilakukan maka nilai variabel pos akan selalu i atau berapa kali perulangan telah dilakukan, sehingga disetiap perulangan nilai pos akan menjadi indeks elemen yang akan dilakukan perbandingan selanjutnya.

baris 15, terdapat perulangan for yang akan mengulang baris 16-17 dengan j sebagai penghitung perulangan, dimana ini berarti perulangan akan selalu di mulai dengan nilai i+1 sehingga memastikan nilai i dan j tidaklah sama dan berada tepat di depan i agar bisa terus dilakukan perbandingan, lalu diakhiri ketika perulangan telah mencapai n kali. 

baris 16 terdapat variabel nilai k dimana ketika elemen arr ke j nilainya kurang dari 50 maka k akan bernilai 50- arr[j], tetapi jika lebih besar dari 60 maka nilai k akan menjadi arr[j]-60, variabel k ini saya gunakan untuk menentukan jarak masing masing umur dari 50 ataupun 60 dari pada perulangan array di tiap elemen

baris 17, terdapat percabangan if dimana jika nilai k dikalikan dengan dirjnya sendiri lebh besar dari nilai 50 dikurangi nilai arr indeks ke pos yaitu indeks ke i yang dikuadratkan, atau ketika k dikalikan dengan dirjnya sendiri lebh besar dari nilai nilai arr indeks ke pos yaitu indeks ke i dikurangi 60 yang dikuadratkan, maka variabel pos yang awalnya memiliki nilai i, akan berganti menajadi memiliki niali j.

baris 18, terdapat percabangan yang berada if, dimana jika pos tidak memiliki nilai yang sama dengan i maka akan memanggil fungsi tukar untuk menukarkan elemen arr indeks i dengan arr indeks ke j

baris 19, terdapat perulangan for yang digunakan untuk mengulang kode baris 20 sebanyak jumlah elemen array m untuk mengurutkan nilai array m dari yang terbesar ke yang terkecil antara angka 50-60.

baris 20, terdapat percabangan if dimana jika nilai array m indeks ke i lebih kecil dari nilai array m indeks ke i+1 maka akan memanggil fungsi tukar untuk menukarkan nilai elemen dari dua indeks tersebut. 

<img width="535" height="215" alt="image" src="https://github.com/user-attachments/assets/f0f9604e-8a74-426d-9cc5-085ca9c78bdb" />

baris 23, terdapat fungsi utama yang berisi logika inti dari program, dimana didalamnya mencakup baris 24-50

baris 24, berisi blok try yang akan memastikan input user di baris 25 sesuai yaitu berupa angka

baris 25, terdapat variavel N yang akan meminta jumlah pasien kepada user dan disimpan ke variabel N

baris 26, terdapat blok exception yang akan mengeksekusi baris 27-28 yaitu menampilkan "Input tidak valid!" dan di baris 28 akan menampilkan ulang baris 25, hal ini akan terus dilakukan hingga user memasukkan input berupa integer dengan benar 

baris 29, 30, 31 terdapat variabel array kosong, yaitu variabel arr, m dan d, arr digunakan untuk menampung angka lebih kecil dari 50 dan lebih besar dari 60. lalu variabel m akan menampung angka lebih besar sama dengan 50 dan lebih kecil sama dengan 60, dan d menampung keseluruhan nilai sebelum di urutkan 

<img width="780" height="454" alt="image" src="https://github.com/user-attachments/assets/03a3fdc4-930d-454b-8b0f-3255e4f2b390" />

baris 32, akan menampilkan "Masukkan umur pasien:"

baris 33, terdapat perulangan for untuk meminta input umur setiap pasien kepada user sebanyak jumlah pasien, dimnana perulangan ini mencakup baris 34-45

baris 34, perulangan while untuk mengulangi blok try-exception, untuk memastikan nput user di baris 36 berupa integer, sehiigga ketika in[ut tidak sesuai, program dapat terus menampilkan permintaan input kembali hingga user memasukkan input yang sesuai, yaitu berupa integer

baris 35 berisi blok try dimana ketika input umur user berupa integer maka akan mengeksekusi baris berikutnya yitu baris 37

baris 36, terdapat variabel permintaan untuk memasukkan input kepada user dan di simpan di variabel umur yang akan menyimpan nilai input user sementara sebelum dipindahkan ke array 

baris 37 terdapat percabangan if dengan kondisi ketika umur bernilai lebih besar sama dengan 50 dan lebih kecil sama dengan 60 maka nilai umur akan dimasukkan ke array m di baris 38, dan array d di baris 39

baris 40 terdapat lanjutan dari percabangan if pada baris 37 dimana ketika kondisi pada percabangan tersebut tidak terpenuhi maka akan akan dieksekusi dan mengeksekusi baris 41 yang menambahkan nilai umur ke array arr dan baris 42 yang akan menambahkan nilai umur ke array d

baris 43, merupakkan penghentian perulangan pada baris 34, yang mana menandakan tidak perlu permintaan ulang untuk memasukkan umur dikarenakan input sebelumnya telah sesuai

baris 44 terdapat baris blok exception yang akan dieksekusi dan mengeksekusi baris 45 yang menampilkan "Input tidak valid, silakan masukkan angka!" ketika input yang diterima di baris 36 tidak berupa integer, lalu setelahnya akan meminta user untuk memasukkan input lagi hingga input sesuai

baris 46 akan menampilkan urutan pasien yang belum diurutkan sesuai standar yang tersimpan di array d

baris 47 terdapat pemanggilan fungsi selection sort yang ada di baris 11

baris 48 terdapat variabel p yang akan menggabungkan array arr dan array m menjadi satu kesatuan array setelah disorting

baris 49 akan menampilkan urutan pasien berdasarkan prioritas umur

baris 50 terdapat perulangan for yang digunakan untuk menampilakan array p satu persatu

<img width="345" height="58" alt="image" src="https://github.com/user-attachments/assets/7b343db5-3923-4406-9068-cfb0c45285e4" />

baris 53 merupakan pengecekan kondisi untuk mengeksekusi baris 41 apakah file sedang di jalankan secara langsung bukan di impor.

baris 54 merupakan pemanggilan fungsi main di baris 23.

# Output
<img width="547" height="101" alt="image" src="https://github.com/user-attachments/assets/10f5c37e-920a-44bf-9143-e45b774f05eb" />

ketika program pertama kali dijalankan akan menampilkan judul program dari source code baris 1-3 dan meminta input jumlah user yang akan di sorting umurnya yang berasal dari source code baris 25

<img width="269" height="131" alt="image" src="https://github.com/user-attachments/assets/88f3847a-0cef-4226-bccb-a49f87f5359a" />

setelah memasukkan jumlah pasien, user akan diminta memasukkan umur masing masing pasien sebanyak jumlah pasien yang dimaksukkan

<img width="745" height="49" alt="image" src="https://github.com/user-attachments/assets/9f6e011b-177d-44b3-a965-36cfc0567653" />

ketika user telah memasukkan seluruh umur pasien, maka akan ditampilkan urutan pasien sebelum di urutkan, dan urutan pasien setelah diurutkan

# Link Penjelasan YouTube
https://youtu.be/pZqO3Xkj0gk?si=7jTat-git6-pC_lT
