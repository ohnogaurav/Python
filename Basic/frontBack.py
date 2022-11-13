a=input('enter a string :- ')
b=len(a)
n=0
for i in range(b,0,-1):
    print(a[n],'  ',a[i-1])
    n+=1
