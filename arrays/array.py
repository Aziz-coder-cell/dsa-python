import array 
x = array.array('i',[10,20,30,20,40,50])
x.append(60)
x.remove(20)
y=[70,80]
x.extend(y)
print(x)
l = list(x)
print(l)
arr = array.array('i')
for i in x[2:]:
    if i!=60:
        arr.append(i)
print(arr) 
