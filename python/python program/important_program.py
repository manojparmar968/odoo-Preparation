# 1. sort a list without any inbuilt method, find lowest number, number in Ascending & Descending order, 
# Note- Ascending order condition 
        # n[] >= n[]
    # Descending order
        # n[] <= n[]
n = [3,2,1,5,4,6,7,8]
# sort a list without any inbuilt method
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] >= n[j]: # Assending order
            n[i],n[j] = n[j],n[i]

            # OR

index = len(n)-1 # Using Bubble Sort Algorithm
for i in range(index):
    for j in range(index-i):
        if n[j] < n[j+1]: # Descending order
            n[j],n[j+1] = n[j+1],n[j]
# Note:-
nums = [2, 3, 1, 5, 6, 4, 0]
print(sorted(nums)) # sorted() will returns a list
print(nums.sort()) # sort() will returns a None, used with only list methods.

# 2. Remove repeat character for string, 
s = "mmaannooj"
result = ""
for char in s:
    if char not in result:
        result += char
print(result)

result = ''.join(sorted(set(s), key=s.index))
print(result)

s1 = ["a", "b", "a", "c", "c"] # o/p = ['a', 'b', 'c']

#Remove repeat character for string
s = "innage" 
print((list(set(s))))

# Remove repeated number from list and count a number how many times apper.
n=[5,2,1,4,3,2,8,4,2,1,2,0]

# using SET
s = list(set(n))
print([[i, n.count(i)] for i in s])

# 
uniq_list = []
r_c = 0
rep_num = []
for i in n:
    if i not in uniq_list:
        uniq_list.append(i)
        r_c = n.count(i)
        rep_num.append(r_c)
print(uniq_list)
print(rep_num)

c = 0
count_list = []
unique_list = []
for i  in range(len(n)):
    if n[i] not in unique_list:
        unique_list.append(n[i])
        c = n.count(n[i])
        count_list.append(c)
print(unique_list)
print(count_list)

#  count and remove duplicates from list and then convert list to dictinory.
l = [11,22,11,30,8,35,8,8,22]

s = list(set(l))
print([[i,l.count(i)] for i in s])

uniq_list = []
c_list = []
for i in l:
    if i not in uniq_list:
        uniq_list.append(i)
        c_list.append(l.count(i))

print(uniq_list)
print(c_list)
d = {}
for k in uniq_list:
    for v in c_list:
        d[k] = v
        c_list.remove(v)
        break
print(str(d))

dd = {}
for i in l:
    if i not in dd:
        dd[i] = 1
    else:
        dd[i] += 1
print(dd)

# 18. n = 123456 Reverse a number & Reverse a string s = 'Manoj'
n = 123456 # Reverse a number
rev = 0
while (n>0):
  a = n % 10
  rev = rev * 10 + a
  n = n//10
print("rev: ",rev)

s = "manoj" # Reverse a string
r = ''
for i in s:
  r = i + r
print(r)
print(s[::-1])

# 24. from given list arr = [-1,0,1,2,3,5,6], find two values which sum is equal to sum = 3.
arr = [-1,0,1,2,3,5,6]
sum = 3
print(len(arr)-1,len(arr))
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == sum:
            print("index of i & j",i,j, 'value: ',arr[i], arr[j])

arr = [2,6,5,8,11]
target = 14

# 28. a = "Hello World @@123" count upper case , lowe case and digits in python
# ORD(): The ord function is used to get the Unicode code point (an integer) for a single character.
# Upper case character: 65-90
# lowe case character: 97-122
# digits: 48-57
a = "Hello World @@123"

upper_count = 0
lower_count = 0
digit_count = 0

for char in a: # Using Build in Function
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1

for char in a: # Without Using Build In Function
    # Uppercase letters: ASCII 65 ('A') to 90 ('Z')
    if 65 <= ord(char) <= 90:
        upper_count += 1
    # Lowercase letters: ASCII 97 ('a') to 122 ('z')
    elif 97 <= ord(char) <= 122:
        lower_count += 1
    # Digits: ASCII 48 ('0') to 57 ('9')
    elif 48 <= ord(char) <= 57:
        digit_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)