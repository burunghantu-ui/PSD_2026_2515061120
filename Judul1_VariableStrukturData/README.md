# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana untuk mendata nama pasien, menentukan id pasien, dan menunjukkan nomor antrian pasien tersebut sehinga membantu dalam pendataan pasien di sebuah klinik. Dalam program ini dapat dilakukan pendataan dengan memasukkan 5 nama pasien, dengan fitur yang ada nomor antrian dan id pasien akan langsung di berikan yang bisa di akses dan ditampilkan melalui menu.

Program ini menggunakan struktrur data list atau array satu dimensi untuk menampung kelima data pasien dalam satu variabel, program ini juga menggunakan looping while agar menu utama dan mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga bisa di tampilkan secara berulang ulang, selain while terdapat 'for' yang juga digunakan untum meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada. Program ini menggunakan percabangan if yang dimana digunakan untuk mementukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini menggunakan manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

# Source Code

<img width="711" height="78" alt="image" src="https://github.com/user-attachments/assets/7dd83259-ebbc-4c4b-9dd7-0f12cad0ead4" />

Baris 1-3 di buat untuk mencetak judul program, serta garis pembatas untuk mempercantik.

<img width="514" height="120" alt="image" src="https://github.com/user-attachments/assets/5f5db598-6cc7-4504-9a2d-dc359b4e6255" />

Baris 5 merupakan fungsi yang dibuat untuk menampikan fitur menu yang terdapat dalam program dan baris 6-9 untuk menampilakan pilihan pilihan fitur yang di wakili oleh angka

<img width="639" height="215" alt="image" src="https://github.com/user-attachments/assets/4ad8b5e5-f5a3-4945-b4cc-dee4befb593c" />

baris 11 adalah fungsi utama yang dimana inti logika dari program dijalankan

baris 12 merupakan deklarasi array dengan variabel a, dan 5 sebagai jumlah kapasitas array.

baris 13 berisi looping while yang mana akan terus menerus melakukan inti logika didalamnya terus menerus hingga memnuhi kondisi berhenti (break, di baris 35), dimana inti logika yang terdapat dari baris 14-40.

baris 14 merupakan panggilan dari fungsi menu di baris 5.

baris 15- 19 merupakan blok exception handling dimana try mengawasi input user yang akan dimasukkan user di baris 16, jika input bukan berupa integer seperti yang diminta maka exception di baris 17 akan menjalankan baris 18 yang akan di tampilkan dan baris 19 yang akan melakukan pengulangan aksi baris 16 hingga user memasukkan data yang valid.

<img width="795" height="125" alt="image" src="https://github.com/user-attachments/assets/e1c60f05-37cd-450e-9072-e43d910dcbc0" />

baris 20 merupakan percabangan if yang akan melakukan aksi didalamnya ketika kondisi terpenuhi, dimana pada baris ini kondisi yang dimaksud ketika choice (input user) adalah 1 maka baris 21-22 yang akan akan di eksekusi

baris 21 merupakan perulangan for yang akan meminta input user untuk dimasukkan ke array 'a' sebanyak 5 kali, dan baris 22 akan menampilkan data pasien saat ini

baris 23 merupakan perpanjangan dari percabangan if sebelumnya dimana jika choice bukan 1 tetapi adalah 2 makan baris 24 yang akan di eksekusi.

baris 24 merupakan perulangan sebanyak 5 kali untuk menampilkan nomor id setiap pasien

<img width="961" height="265" alt="image" src="https://github.com/user-attachments/assets/15178199-1fad-4741-bb37-d33fad0870fe" />

baris 25 ketika choice adalah 3 maka baris 26-35 akan dieksekusi

baris 26 merupakan looping while dimana logika didalamnya baris 25-35 akan terus di eksekusi hingga break, dimana digunakan untuk mengulang program hingga user memasukan input yang sesuai.

baris 27 juga eksekusi berulang baris 28-32 yang berupa blok exception handling, dimana dalam try (28) baris 29 akan meminta input user, jika input tidak berupa angka atau integer maka baris 30 akan dilewati dan exception(31) akan di eksekusi dimana didalamnya, baris 32 akan ditampilkan dan akan kembali mengeksekusi baris 28-32 terus menerus hingga input user  berupa integer dan akhirnya dapat mengeksekusi baris 30 yaitu break.

<img width="939" height="57" alt="image" src="https://github.com/user-attachments/assets/6e171073-8e3c-4a40-a029-204834b32943" />

baris 33 merupakan percabangan dimana jika nilai input user sama atu tidak melebihi jumlah kapasitas array maka akan menampilkan nomor antrian milik pasien, dimana nomor pasien disini adalah nomor indeks nilai array yang di input user di kurangi 1, lalu perulangan while pada baris 26 akan dihentikan di sintaks break.

baris 34 dieksekusi ketika input user di baris 29 ketika melebihi batas jumlah array, maka akan ditampilakn 'tidak ada nomor urut tersebut!' dan program akan kembali mengeksekusi baris 27-34 hingga input user sesuai dan tidak melebihi batas jumlah array

<img width="493" height="101" alt="image" src="https://github.com/user-attachments/assets/0fce6ab9-8b08-4b45-9218-a690daf9d813" />

baris 35 ketika choice adalah 4 maka baris 36-38 akan dieksekusi

baris 36 akan menampilkan "Program selesai."

baris 37 atau break digunakan untuk menghentikan perulangan while di baris 13

baris 38 adalah ketika input user yaitu choice di baris 16 tidak memenuhi seluruh kondisi percabangan yaitu 1-4 maka akan di tampilkan "Pilihan tidak valid!" dan mengeksekusi ulang seluruh program di dalam while(13) hingga kondisi pada baris 35 terpenuhi.

<img width="336" height="48" alt="image" src="https://github.com/user-attachments/assets/a439fe6a-1e7a-4825-8a5f-521330e92d79" />

baris 40 merupakan pengecekan kondisi untuk mengeksekusi baris 41 apakah file sedang di jalankan secara langsung bukan di impor.

baris 41 merupakan pemanggilan fungsi main di baris 11.


# Output

<img width="541" height="229" alt="image" src="https://github.com/user-attachments/assets/84c6ac47-05ad-401f-9d03-96058a5b83d5" />

merupakan output yang keluar dari baris 1-3 dan 14 yang menampilkan fungsi menu di baris 5, lalu output yang meminta input 'pilihan' berasal dari sorce code baris 15 

<img width="547" height="184" alt="image" src="https://github.com/user-attachments/assets/8b52090b-e642-4b27-b463-08c4ccdaf1ac" />

mrupakan output yang dihasilkan ketika user memasukkan input angka 1 yang mana memenuhi kondisi baris 20 akan mengeksekusi baris baris 20 dan akan menampilkan perulangan dari baris 21 yang meminta input ke user lalu menampilkan baris 22

<img width="316" height="147" alt="image" src="https://github.com/user-attachments/assets/c554abb1-4f8a-46c4-81be-f945794a2e66" />

merupakan output ketika user memasukkan input 2 yang mana akan memenuhi kondisi di baris 23 menampilkan perulangan dari baris 24

<img width="460" height="105" alt="image" src="https://github.com/user-attachments/assets/0dbbed1a-3a1d-40b3-8c72-21dee7c55d9c" />

merupakan output ketika user memasukkan input 3 yang mana akan memenuhi kondisi di baris 25 dan meminta input kepada user, dimana output ini berasal dari baris 29, setelah memasukkan input, selanjutnya akan menampilkan source code dari baris 33 sesuai dengan input dari user.

<img width="460" height="50" alt="image" src="https://github.com/user-attachments/assets/efa7eee5-5191-47f5-830c-037ef808effb" />

jika user memasukkan yang bukan angka atau integer maka akan menampilkan output yang berasal dari source code baris 32 yang merupakan blok exception handling dan akan kembali menampilkan permintaan input dari baris 29 

<img width="445" height="43" alt="image" src="https://github.com/user-attachments/assets/50749835-5467-4d19-9d9e-7dfec3313205" />

output ketika user memasukkan angka lebih dari kapasitas jumlah data array yang ada

<img width="381" height="196" alt="image" src="https://github.com/user-attachments/assets/91021448-1358-4a1d-8ec0-db35026f2f57" />

ketika user memasukkan input 'pilihan' lebih dari 4 atau tidak sesuai dengan pilihan yang ada maka akan menampilkan baris 38 dan kembali meminta input kepada user

<img width="266" height="60" alt="image" src="https://github.com/user-attachments/assets/ca1eeb37-03ff-4c56-9a8a-68df4ce44725" />

dan ketika user memasukkan pilihan bukan berupa angka akan mengeluarkan output dari baris 18 yang merupakan blok exception handling

# Link YouTube

untuk penjelasan lebih lengkap dapat dilihat pada video berikut

