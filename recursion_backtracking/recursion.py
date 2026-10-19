#Basic
"""def recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursion(n-1)+recursion(n-2) 
    
print(recursion(5))"""

#Intermediate
"""def hanoi(n,source,auxiliary,destination):
    if n==1:
        print(f"Move disk 1 from {source} to {destination}") 
        return
    hanoi(n-1,source,destination,auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1,auxiliary,source,destination)

if __name__ == '__main__':
    hanoi(4, 'A', 'B', 'C')"""
    
#Advance
def count_paths(s):
    if len(s)==0:
        return 1
    if s[0]=='0':
        return 0
    ways = 0 
    ways += count_paths(s[1:])
    if len(s)>=2 and 10<=int(s[0:2])<=26:
        ways += count_paths(s[2:])
    return ways

print(count_paths('123'))