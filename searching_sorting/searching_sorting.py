#Basic
"""data = [15, 8, 2, 42, 10, 5]
target = 42
i=0
while  i<len(data) :
    if data[i] == target:
        print("Target found at index",i)
        break
    i=i+1
else:
    print("Target not found")"""

#Intermediate
"""data = [2, 5, 8, 10, 15, 42]
target = 15
low = 0
high = len(data)-1
while low<=high:
    mid=(low+high)//2
    if data[mid]==target:
        print("Target found")
        break
    elif data[mid] < target:
        low = mid+1
    else:
        high=mid-1
else:
    print("Target not found")"""

#Advance
def divide(data):
    if len(data) <= 1:
        return data
    
    mid = len(data)//2

    left_half = data[:mid]
    right_half = data[mid:]

    left_half = divide(left_half)
    right_half = divide(right_half)

    return merge(left_half,right_half)

def merge(left_half,right_half):
    i = j = 0
    sorted = []
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<=right_half[j]:
            sorted.append(left_half[i])
            i= i + 1
        else:
            sorted.append(right_half[j])
            j=j+1
    if left_half:
        sorted.extend(left_half[i:])
    if right_half:
        sorted.extend(right_half[j:])
    return sorted
        
data = [12, 11, 13, 5, 6, 7]
result = divide(data)
print(result)