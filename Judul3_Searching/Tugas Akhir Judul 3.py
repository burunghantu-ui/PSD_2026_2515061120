print('=========================================================')
print('                   ADMINISTRASI KLINIK                     ')
print('=========================================================')

def search(pasien, jml, target, indeks):
    count=0
    i = 0
    while i < jml :
        if pasien[i]==target: 
            count = count + 1
            indeks.append(i)
        i+=1
    return count
    
def main():
    pasien=[]
    indeks=[]
    while True:
        try:
            jml = int(input('masukkan jumlah pasien: '))
            break
        except ValueError:
            print('masukkan angka!')
    for i in range(jml): 
        nama = input('masukkan nama pasien: ')
        pasien.append(nama)
    target = input('masukkan nama pasien yang ingin dicari: ')
    count = search(pasien, jml, target, indeks)
    if count > 0:
        print(f'pasien {target} ditemukan {count} kali di urutan - ', end=' ')
        for i in range(len(indeks)): print(indeks[i]+1, end=' ')
    else: print(f'pasien {target} tidak terdapat di antrian')

main()