# Count All The 2 From given array and remove duplicate from arry.
arr=[0,1,2,2,3,4,5,6,2,7,8,9,2,8,7,0]


uniq_arr = []
dup_arr = []
for i in arr:
    if i not in uniq_arr:
        uniq_arr.append(i)
    elif i not in dup_arr:
        dup_arr.append(i)
print(uniq_arr)
print(dup_arr)