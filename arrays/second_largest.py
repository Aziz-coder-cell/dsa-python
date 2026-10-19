arr = [20, 20, 10]
largest = float('-inf')
second_largest = float('-inf')  
for i in range(1, len(arr)-1):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i] 
    else:
        continue
if second_largest == largest:
    print("There is no second largest element in the array.")
    print(-1)