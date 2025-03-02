n = 20
# , o/p = 1 2 3 4 tom 6 cat 8 9 tom 11 12 13 cat tom 16 17 18 19 tom
# i%5 == 0 tom
# i%7 ==0 cat

for i in range(1,n+1):
    if i%5 == 0:
        i = 'tom'
    elif i%7 == 0:
        i = 'cat'
    print(i)