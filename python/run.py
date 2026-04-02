# remove duplicates from sorted list.
l = [5,5,7,8,8,9,9,10,10]

n =[]

for i in l:
    if i not in n:
        n.append(i)
print(n)