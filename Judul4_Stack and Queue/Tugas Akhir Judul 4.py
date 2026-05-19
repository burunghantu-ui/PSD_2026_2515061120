class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Antrian:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None
    
    def tambah(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

    def hapus(self):
        if self.is_empty():
            print("antrian kosong")
            return
        temp = self.front_ptr
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None
        return temp.data

    def display(self):
        if self.is_empty():
            print("antrian kosong")
            return
        print("Antrian: ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

class riwayatpasien:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def pop(self):
        if self.is_empty():
            print("riwayat antrian pasien kosong")
            return
        temp = self.top_ptr
        self.top_ptr = self.top_ptr.next
        return temp.data

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_ptr
        self.top_ptr = new_node

    def clear(self):
        self.top_ptr= None
        print('riwayat di kosongkan!')

    def display(self):
        if self.is_empty():
            print("riwayat antriann pasien kosong")
            return
        print("riwayat antrian pasien (dari yang terbaru): ", end="")
        current = self.top_ptr
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def menu():
    print("\n1. antrian")
    print("2. riwayat antrian pasien")
    print("3. lihat antrian dan riwayat")
    print("4. keluar")

def menuantri():
    print('\n1. tambah antrian')
    print('2. antrian terdepan telah di layani')
    print("3. melihat antrian saat ini")
    print("4. keluar")

def riwayatantrian():
    print('\n1. melihat riwayat')
    print('2. undo')
    print("3. bersihkan riwayat")
    print("4. keluar")

def main():
    antri = Antrian()
    riwayat = riwayatpasien()
    print('=========================================================')
    print('                   ADMINISTRASI KLINIK                     ')
    print('=========================================================')

    while True:
        menu()
        while True:
            try:
                pilihan= int(input("pilih: "))
                break
            except ValueError:
                print('input tidak valid!')
        if pilihan == 1:
            while True:
                menuantri()
                try:
                    pilih = int(input("pilih: "))
                except ValueError:
                    print('input tidak valid!')
                    continue
                if pilih == 1:
                    pasien = input('masukkan nama pasien: ')
                    antri.tambah(pasien)
                elif pilih == 2:
                    k = antri.hapus()
                    riwayat.push(k)
                    print(f"pasien {k} telah dilayani")
                elif pilih==3:
                    antri.display()
                elif pilih == 4:
                    break
                else: 
                    print("input tidak valid!")

        elif pilihan == 2:
            while True:
                riwayatantrian()
                try:
                    pil = int(input('pilih: '))
                except ValueError:
                    print('input tidak valid!')
                    continue
                if pil==1:
                    riwayat.display()
                elif pil==2:
                    b = riwayat.pop()
                    antri.tambah(b)
                    print(f"riwayat pasien {b} berhasil di batalkan")
                elif pil ==3:
                    riwayat.clear()
                elif pil == 4:
                    break
                else:
                    print("input tidak valid!")

        elif pilihan == 3:
            antri.display()
            riwayat.display()

        elif pilihan ==4: 
            break
        else: 
            print("input tidak valid!")

main()