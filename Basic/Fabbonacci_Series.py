a=0
b=1
print(a,end=' ')
print(b,end=' ')
n=0
while n<8:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    n+=1
