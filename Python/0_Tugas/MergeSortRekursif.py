def merge_sort(arr):
    if len(arr) > 1:
        # Bagi array menjadi dua bagian
        tengah = len(arr) // 2
        setengah_kiri = arr[:tengah]
        setengah_kanan = arr[tengah:]

        # Rekursif untuk mengurutkan kedua bagian
        merge_sort(setengah_kiri)
        merge_sort(setengah_kanan)
    
        # Gabungkan kedua bagian yang sudah diurutkan
        i = j = k = 0
        print("kanan ", setengah_kanan)
        print("kiri ", setengah_kiri)
        # Bandingkan elemen dari setengah_kiri dan setengah_kanan
        while i < len(setengah_kiri) and j < len(setengah_kanan):
            if setengah_kiri[i] < setengah_kanan[j]:
                arr[k] = setengah_kiri[i]
                i += 1
            else:
                arr[k] = setengah_kanan[j]
                j += 1
            k += 1

        # Jika masih ada elemen tersisa di setengah_kiri
        while i < len(setengah_kiri):
            arr[k] = setengah_kiri[i]
            i += 1
            k += 1

        # Jika masih ada elemen tersisa di setengah_kanan
        while j < len(setengah_kanan):
            arr[k] = setengah_kanan[j]
            j += 1
            k += 1

# Contoh penggunaan
arr = [38, 27, 43, 31, 9, 82, 10]
print("Array sebelum diurutkan:", arr)
merge_sort(arr)
print("Array setelah diurutkan:", arr)