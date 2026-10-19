arr= [100,200,150,300,400]
if len(arr) <= 0:
    print(0)
else:
    avg = arr[0]
    count = 0
    for i in range(1,len(arr)):
        if arr[i] > avg/i:
            count += 1
        avg += arr[i]
print(count)

