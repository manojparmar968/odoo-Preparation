# 1  sum is equal to the target.
arr = [2,6,5,8,11]
target = 14

print("len(arr)-1 = ",len(arr)-1,"& len(arr) = ",len(arr))
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"the target value of sum {arr[i]} & {arr[j]}",i,j)

# 2.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 9
# output = (1,8)(2,7)(3,6)(4,5)

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            print(nums[i],nums[j])

# 3.