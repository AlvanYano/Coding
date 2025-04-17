def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Angka terbesar akan "menggelembung" ke kanan
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Contoh pakai
data = [5, 3, 8, 4, 11,111,1,1111,11111,1212,121212,1111,2]
bubble_sort(data)
print("Hasil urutan:", data)
