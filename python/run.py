# Count All The 2 From given array and remove duplicate from arry.
arr=[0,1,2,2,3,4,5,6,2,7,8,9,2,8,7,0]

count = 0
lst = []

for i in arr:
    if i not in lst:
        lst.append(i)
        count = arr.count(2)
print(count)
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