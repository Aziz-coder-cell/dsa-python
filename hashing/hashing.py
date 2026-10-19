hash_table = {
    "apple" : 1,
    'banana' : 2,
    'cherry' : 3
}

#Basic
"""print(hash_table['banana'])
if 'grape' in hash_table:
    print('True')
else:
    print('False')
"""

#Intermediate
"""hash_table['apple'] = 10 
print(hash_table.get('grape',0))
print(hash_table)"""

#Advance 
data = [1, 5, 2, 1, 5, 5, 2]
count = {}
for i in data[:]:
    count[i] = count.get(i,0) + 1
print(count)

print(max(count.values()))
print(max(count,key = count.get))