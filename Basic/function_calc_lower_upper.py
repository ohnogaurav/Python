def calclowerupper(a):
    n=len(a)
    length=lowercase=uppercase=0
    while length<n:
        if a[length].islower()==True:
            lowercase+=1
            length+=1
        elif a[length].isupper()==True:
            uppercase+=1
            length+=1
        else:
            length+=1
    return uppercase,lowercase


strng=input('Enter a String:')
x,y=calclowerupper(strng)
print('Lowercase Letters are',y)
print('Uppercase Letters are',x)

