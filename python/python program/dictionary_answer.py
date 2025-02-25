# 1. sort the dict based on number's
dict1 = {'India': 2, 'Us': 1, 'Uk': 3, 'Loser': 5}
dd = {}
for k, v in sorted(dict1.items(), key=lambda item: item[1]):
    dd[k] = v
print(dd)
print({k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])})

# 2. count the frequency of each element in a list.
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency = {}
for i in nums:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# 3. count and remove duplicates from list and then convert list to dictinory.
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

# 4. l=['a','b','b','a','c','b'] convert list to dictinory.
t=['a','b','b','a','c','b']

dd = {}
for x in t:
    if x in dd:
      dd[x] += 1
    else:
      dd[x] = 1
print(dd)