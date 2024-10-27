def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr1)
print("Quick sort:", quick_sort(arr1.copy()))