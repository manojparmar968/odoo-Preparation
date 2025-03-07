# 1. Make 2 list in 1 list, don't have duplicate values, & without any loop
l1 = [1,3,5,7,8,10]
l2 = [2,3,4,6,8,9,10]
print(list(set(l1+l2)))

# 2. Find common elements between two lists.
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
lst = []
for i in list_a:
    if i in list_b:
        lst.append(i)
print(lst)

# 3. sort a list without any inbuilt method, find lowest number, number in Ascending & Descending order, 
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

# 4. count a total number in n = 123654
n = 123654
count = 0
while(n>0):
    count += 1
    n = n//10
    # print("n = ",n,"count = ",count)
print("total number of digits", count)

# 5. count even and odd from given list, l = [1,2,3,8,9,5,7,6,4] and seprate even and odd numbers.
l = [1,2,3,8,9,5,7,6,4]
even = []
odd = []
even_count = 0
odd_count = 0
for i in l:
    if i%2 == 0:
        even_count += 1
        even.append(i)
    else:
        odd_count += 1
        odd.append(i)
print("even count: ",even_count,sorted(even))
print("odd count: ",odd_count,sorted(odd))

# 6. n = 20, o/p = 1 2 3 4 tom 6 cat 8 9 tom 11 12 13 cat tom 16 17 18 19 tom
for i in range(1,20+1):
    if i % 5 == 0 or i % 10 == 0:
        i = 'tom'
    elif (i % 7 == 0) or (i % 14 == 0):
        i = "cat"
    print(i)

# 7. Count All The 2 From given array and remove duplicate from arry.
arr=[0,1,2,2,3,4,5,6,2,7,8,9,2,8,7,0]
"""
Count All The 2 From given array
"""
arr=[1,2,2,3,4,5,6,2,7,8,9,2,8]
count = 0
match = 2
for i in range(len(arr)):
    if arr[i] == match:
        count = count+1
print("count",count)
"""
Remove Duplicate from array
"""
count = 0
lst = []

for i in arr:
    if i not in lst:
        lst.append(i)
        count = arr.count(2)
print("count of 2 is: ",count)
print(lst)

uniq_list = []
count_comm_list = []
c = 0
for i in arr:
    if i not in uniq_list:
        uniq_list.append(i)
        c = arr.count(i)
        count_comm_list.append(c)
print(uniq_list)
print(count_comm_list)

uniq_arr = []
dup_arr = []
for i in arr:
    if i not in uniq_arr:
        uniq_arr.append(i)
    elif i not in dup_arr:
        dup_arr.append(i)
print(uniq_arr)
print(dup_arr)

# 8. the factorial of 6 is 1*2*3*4*5*6 = 720.
num = 6
fact = 1
if num < 0:
    print("Factoril is Not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact *= i
    print("Factoril is = ", fact)

# 9. calcualte a given year is a leap year. year = 1994,2017,2024
# year = 1994
# year = 2017
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# 10. 
i = "manoj_parmar_india.json" # o/p = India
s = "LoserManoj@321" # o/p = 123
print(i.split('_'))
print(i.split('_')[::-1])
print(i.split('_')[::-1][0])
print(i.split('_')[::-1][0].split('.'))
print(i.split('_')[::-1][0].split('.')[0])
print(i.split('_')[::-1][0].split('.')[0].capitalize())

# 11. Remove repeat character for string, 
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

# 12. Remove repeated number from list and count a number how many times apper.
n=[5,2,1,4,3,2,8,4,2,1,2,0]
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

# 13. l = [11,22,11,30,8,35,8,8,22] count and remove duplicates from list.
# count and remove duplicates from list and then convert list to dictinory.
l = [11,22,11,30,8,35,8,8,22]
d = {}
unique_list = []
common_list = []
c = 0
for i in l:
  if i not in unique_list:
    unique_list.append(i)
    c = l.count(i)
    common_list.append(c)
print(unique_list,common_list)
for key in unique_list:
  for value in common_list:
    d[key] = value
    common_list.remove(value)
    break
print(str(d))

# 14. l=['a','b','b','a','c','b'] convert list to dictinory.
t=['a','b','b','a','c','b']

dd = {}
for x in t:
    if x in dd:
      dd[x] += 1
    else:
      dd[x] = 1
print(dd)

# 15. remove duplicates from a list.nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
dup_list = []
unique_list = []
c = 0
for i in nums:
    if i not in unique_list:
        unique_list.append(i)
        c = nums.count(i)
        dup_list.append(c)

        # OR

for i in range(len(nums)):
    if nums[i] not in unique_list:
        unique_list.append(nums[i])
        c = nums.count(nums[i])
        dup_list.append(c)
print(unique_list)
print(dup_list)

# 16. l = [11,22,30,8,35] #if > 20 -1, < 20 -2 using list comphersion. o/p = [9, 21, 29, 6, 34]
l = [11,22,30,8,35] #if > 20 -1, < 20 -2
print([x-1 if x > 20 else x-2 for x in l])

# 17. lst = [1, 2, 3, 4, 5] reverse a list, without any built in function or slicing.
lst = [1, 2, 3, 4, 5]
# reverse a list, without any built in function or slicing.
r_list = []
for value in lst:
    r_list = [value] + r_list
print("List after reverse : ", r_list)

# Reverse build in method using method
print(lst[::-1])

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

# 19. Middle Element in a List. numList = [1, 2, 3, 4, 5,6,7]
numList = [1, 2, 3, 4, 5,6,7]
midElement = int((len(numList)/2)) 
print(numList[midElement])

# 20. Counting the occurrences of elements in the list. days = ['S','M','M','M','F','S']
days = ['S','M','M','M','F','S']
y = set(days)
print([[i,days.count(i)] for i in y])

# 21. Find Missing Number, n = [1, 2, 3, 5, 6, 7, 8, 9,10,11,13,14,16]
n = [1, 2, 3, 5, 6, 7, 8, 9,10,11,13,14,16]
num = set(n)
op = []
for i in range(1, n[-1]):
    if i not in num:
        op.append(i)
print(op)

# 22. Find Duplicate Number in an Array, lis = [1, 2, 2, 3, 4, 4, 4, 5, 5]
lis = [1, 2, 2, 3, 4, 4, 4, 5, 5]
uniq_list = []
dup_list = []

for i in lis:
    if i not in uniq_list:
        uniq_list.append(i)
    elif i not in dup_list:
        dup_list.append(i)
print(dup_list)

# 23. Find the number occurring odd number of times, lis = [1, 1, 2, 2, 3, 3, 3]
lis = [1, 1, 2, 2, 3, 3, 3]
res = 0
for i in lis:
    res = res ^ i
print(res)

# 24. from given list arr = [-1,0,1,2,3,5,6], find two values which sum is equal to sum = 3.
arr = [-1,0,1,2,3,5,6]
sum = 3
print(len(arr)-1,len(arr))
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == sum:
            print("index of i & j",i,j, 'value: ',arr[i], arr[j])

# 25.  sum is equal to the target.
arr = [2,6,5,8,11]
target = 14

print("len(arr)-1 = ",len(arr)-1,"& len(arr) = ",len(arr))
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"the target value of sum {arr[i]} & {arr[j]}",i,j)

# 26.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 9
# output = (1,8)(2,7)(3,6)(4,5)

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            print(nums[i],nums[j])

# 27. From given list my_list = [[0, 1, 2, 3] for i in range(2)],  print the output 3
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[1][3])

"""
* * * * *
* * * *
* * *
* *
*
"""
n = 5
for i in range(0,n+1):
    for j in range(1, n-i+1):
        print("*",end=" ")
    print()

"""
        *
      * *
    * * *
  * * * *
"""
n = 5
k = (n*2) - 2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k = k -2
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")

"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")

for i in range(0,n+1):
    for j in range(0,i-1+1):
        print("*",end=" ")
    print()

"""
     *
    ***
   *****
  *******
   *****
    ***
     *
"""
h = 7

if h%2 == 0:
    print("Enter the height odd number")
else:
    middle_row = (h+2)//2
    for i in range(middle_row):
        print(" " * (middle_row-i), "*" * (i*2+1))

    for i in range(middle_row-2,-1,-1):
        print(" " * (middle_row-i), "*" * (i*2+1))

"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""
k=1
i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ",end=" ")
        b=b+1
    j=1
    while(j<=k):
        print(j,end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1



# flyod
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
count = 1

for i in range(1,n+1):
    for j in range(0,i):
        print(count,end=" ")
        count += 1
    print()

# print triangle height 5.
n = 5
for x in range(n):
    print(" " *(n-x-1) + "*" * (2*x+1))
