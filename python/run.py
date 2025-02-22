# lst = [1,4,2,1,12,6,7,11,10,21] 
# op = [2,6,10]


n=[5,2,1,4,3,2,8,4,2,1,2,0]
count = 0
c = []
l=[]
for i  in range(len(n)):
    if n[i] not in l:
        l.append(n[i])
        count = n.count(n[i])
        c.append(count)

print(count)
print(c)
print(l)