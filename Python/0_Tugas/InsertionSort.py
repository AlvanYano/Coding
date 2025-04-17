def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemen yang sedang dibandingkan
        j = i - 1

        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Tempatkan key di posisi yang tepat
        arr[j + 1] = key

# Contoh penggunaan
data = [7, 3, 5, 2, 8]
insertion_sort(data)
print("Hasil urutan:", data)
