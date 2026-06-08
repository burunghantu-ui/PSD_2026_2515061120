class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE #tidak keluar dari jumlah pengecekan
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return False, None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return True, self.table[i]
        return False, None

    def remove_key(self, key):
        bool, entry = self.search(key)
        if entry is None and bool is False:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\ndaftar informasi antrian pasien")
        for i in range(self.SIZE):
            print(f"{i+1}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")

def menu():
    print('\n1. melihat daftar pasien')
    print('2. menambahkan pasien')
    print('3. mencari pasien')
    print('4. menghapus pasien')
    print("5. keluar")


def main():
    dftrpasien = HashMapOpenAddressing()
    dftrpasien.insert(12, "maya: influenza")
    dftrpasien.insert(36, "kei: usus buntu")
    dftrpasien.insert(88, "raya: kanker otak")

    print('=========================================================')
    print('                   ADMINISTRASI KLINIK                     ')
    print('=========================================================')

    while True:
        menu()
        while True:
            try:
                pil= int(input("pilihan: "))
                break
            except ValueError:
                print('masukkan angka')

        if pil == 1:
            dftrpasien.display()
        elif pil == 2 :
            while True:
                try:
                    kode = int(input('masukkan kode unik pasein(angka): '))
                    break
                except ValueError:
                    print("kode harus berupa angka")
            nilai= input("masukkan nama dan penyakit pasien (nama: penyakit): ")
            dftrpasien.insert(kode, nilai)

        elif pil == 3:
            while True: 
                try:
                    cari= int(input("masukkan kode pasien: "))
                    break
                except ValueError:
                    print('kode harus berupa angka!')
            bool, hasil = dftrpasien.search(cari)
            if hasil is not None:
                print(f"\ninformasi pasien {cari} | {hasil.value}")
            else:
                print(f"\nData pasien dengan kode {cari} tidak ditemukan")

        elif pil == 4:
            while True:
                try:
                    cari= int(input("masukkan kode pasien: "))
                    break
                except ValueError:
                    print('kode harus berupa angka!')
            bool, hasil= dftrpasien.search(cari)
            if bool is True:
                print(f"pasien {cari} | {hasil.value} berhasil di hapus")
            else:
                print(f"\nData pasien dengan kode {cari} tidak tersedia")
            dftrpasien.remove_key(cari)

        elif pil == 5:
            break
        else:
            print("pilihan anda tidak valid!")

if __name__ == "__main__":
    main()