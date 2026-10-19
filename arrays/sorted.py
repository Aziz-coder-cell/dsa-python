arr = [1, 2, 3, 4, 5]
i = 0
while i<len(arr)-1:
    if arr[i] < arr[i+1]:
        i += 1
    else:
        print("Array is not sorted in ascending order.")
        break
else:
    print("Array is sorted in ascending order.")