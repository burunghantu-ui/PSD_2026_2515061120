# Administrasi Klinik
## Deskripsi Singkat
Program ini merupakan program sederhana untuk mendata pasien berdasarkan umur untuk ditentukannya antian pelayanan, dimana pasien di bawah 50 tahun dan lansia di atas 60 tahun akan di prioritaskan berdasarkan seberapa jauh jarak umur dari batasan yang telah ditetapkan tersebut, jika ada kesamaan jarak umur pasien dari ketentuan maka akan diurutkan berdasarkan urutan input, sedangkan pasien umur 50-60 akan ditempatkan diakhir dan diurutkann sesuai urutan angka dari terbesar yaitu 60-50.

Program ini menggunkan metode sorting selection yang menggunakan elemen acuan sebagai pembanding dengan elemen lain, sehingga cocok dengan kebutuhan program. hal pertama yang akan ditampilkan dari program ini adalah judul program diikuti dengan meminta user memasukkan jumlah pasien lalu meminta umur pasien sebanyak jumlah pasien menggunakan perulangan for, lalu data tersebut akan diurutkan dalam fungsi selection sort, pada program ini saya memisahkan data menjadi 2 array, dimana yang satu elemennya benilai tidak lebih dari 49 dan lebih besar dari 60, lalu yang lai berisi angka 50-60 sehingga umur 50-60 dapat saya tempatkan diakhir antrian.

Menggunakan looping while untuk mengantisipasi adanya input yang tidak sesuai dengan yang di arahkan sehingga memanggil blok exception dan bisa di tampilkan secara berulang ulang, selain while terdapat 'for' yang juga digunakan untuk meminta input dan menampilkan data berulang sesuai dengan jumlah data yang ada. Program ini menggunakan percabangan if yang dimana digunakan untuk mementukan keputusan perilaku berdasarkan suatu kondisi, selain if di program ini juga terdapat manajemen error yaitu try-except yang digunakan untuk memastikan type data input user sesuai dengan yang di minta.

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

