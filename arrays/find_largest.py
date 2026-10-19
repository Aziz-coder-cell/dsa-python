arr = [3, 8, 1, 6, 9, 2]
max = arr[0]
for i in range(1,len(arr)):
    if arr[i] > max:
        max = arr[i]
print("Maximum value in the array is:", max)
     