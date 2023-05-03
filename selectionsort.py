def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr1 = []
n = int(input("Enter length of the array: "))
for i in range(n):
    tp = int(input("Enter number: "))
    arr1.append(tp)

arr1 = selection_sort(arr1)

print(arr1)