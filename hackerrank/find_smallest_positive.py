arr = [3, 4,5, -1, 1]
n = len(arr)
i = 0 
while i<n:
    correct = arr[i]-1
    if 1 <= arr[i] <= n and arr[i] != arr[correct]:
        arr[i], arr[correct] = arr[correct], arr[i]
    else:
        i += 1

for i in range(n):
    if arr[i] != i+1:
        print(i+1)
        break
else: 
    print(n+1)