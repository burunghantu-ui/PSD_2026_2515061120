print('=========================================================')
print('                   ADMINISTRASI KLINIK                     ')
print('=========================================================')

def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr,N, m):
    n = N - len(m)
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            k = 50 - arr[j] if arr[j]<50 else arr[j]-60
            if k*k > (50-arr[pos])*(50-arr[pos]) or k*k > (60-arr[pos])*(60-arr[pos]): pos = j
        if pos != i: tukar(arr, i, pos)
    for i in range(len(m)-1):
        if m[i]<m[i+1]: tukar(m, i, i+1) 
    

def main():
    try:
        N = int(input("Masukkan jumlah pasien: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    m = []
    d = []
    print("Masukkan umur pasien:")
    for i in range(N):
        while True:
            try:
                umur = int(input())
                if umur >= 50 and umur <= 60:
                    m.append(umur)
                    d.append(umur)
                else:
                    arr.append(umur)
                    d.append(umur)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!") 
    print(f"pasien sebelum diurutkan berdasarkan prioritas umur: {d}")
    selection_sort(arr,N, m)
    p= arr+m
    print("urutan antrian pasien berdasarkan prioritas umur:", end=" ")
    for i in range(N): print(p[i], end=" ")


if __name__ == "__main__":
    main()