print('=========================================================')
print('                   ADMINISTRASI KLINIK                     ')
print('=========================================================')

def menu():
    print("\n1. Masukkan nama pasien")
    print("2. Tampilkan id pasien")
    print("3. tampilkan nomor antrian pasien")
    print("4. keluar")

def main():
    a = [0] * 5
    while True:
        menu()
        try:
            choice = int(input("\nPilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            for i in range(5): a[i] = str(input('Masukkan 5 pasien: '))
            print(f'pasien saat ini: {a}')
        elif choice == 2:
            for i in range(5): print(f"id pasien {a[i]}: id{id(a[i])}")
        elif choice == 3:
            while True:
                while True:
                    try:
                        k = int(input('\nmasukkan nomor antrian yang ingin di cek (1-5) '))
                        break
                    except ValueError:
                        print("Masukkan angka yang valid!")
                if k <= len(a): print(f'nomor antrian {k} milik pasien {a[k-1]}'); break
                else: print('tidak ada nomor urut tersebut!')
        elif choice == 4:
            print("Program selesai.")
            break
        else: print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()