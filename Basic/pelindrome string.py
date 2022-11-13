a=input()#dad
b=len(a)#3
c=(-1)
for i in range(b):#0 1 2 
    if a[i]!=a[c]:
        print('not a pelindrome')
        break
    c=c-1
else:
    print('pelindrome')
