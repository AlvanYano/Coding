def merge(left, right):
    result = []
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    result.extend(left or right)
    return result

def merge_sort(arr):
    width = 1
    while width < len(arr):
        for i in range(0, len(arr), 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2
    return arr

# Contoh penggunaan
arr = [38, 27, 43, 3, 9, 812, 10]
print("Array sebelum diurutkan:", arr)
arr = merge_sort(arr)
print("Array setelah diurutkan:", arr)
