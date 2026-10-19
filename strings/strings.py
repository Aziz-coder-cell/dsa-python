#Intermediate
"""s = "Data-Structures and Algorithms"
s=s.replace('-',' ')
print(s)
str = s.split()
print(str)
str1 = '_'.join(str)
print(str1)"""

#Advance
import re
phrase = "A man, a plan, a canal: Panama"
phrase_lower = phrase.lower()
new_string = re.sub(r"[ ,:]","",phrase_lower)
print(new_string)
rev = new_string[::-1]
print(rev)
if new_string == rev:
    print("true")
else:
    print("false")