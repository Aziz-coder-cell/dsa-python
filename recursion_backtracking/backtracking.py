"""#Basic 
def subset(nums,index,current_list=[],result=[]):
    if index==len(nums):
        result.append(current_list[:])
        return
    current_list.append(nums[index])
    subset(nums,index+1,current_list,result)
    current_list.pop()
    subset(nums,index+1,current_list,result)

    return result

nums = [1,2,3]
index = 0 
print(subset(nums,index))
"""

            #Intermediate 

#Not optimized 
def climb_stairs(n):
    if n==0 or n ==1:
        return 1
    return climb_stairs(n-2) + climb_stairs(n-1)
print(climb_stairs(5))

#Optimized
def climb_stairs(n,memo):
    if n==0 or n ==1:
        return 1
    if n in memo:   
        return memo[n]
    memo.get(n,0) 
    memo[n] = climb_stairs(n-2,memo) + climb_stairs(n-1,memo)

    return memo[n]

memo = {}
print(climb_stairs(5,memo))