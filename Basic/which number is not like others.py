def uni(b):
    a=list(b)
    length=len(a)

    unique=list()
    duplicate=list()
    n=1
    try:
        for i in range(length):
            if n==1:
                unique.append(a[i])
                n+=1
            elif a[i] not in unique:
                unique.append(a[i])
            elif a[i] in unique:
                unique.remove(a[i])
        print(unique)
    except:
        print('No unique value')
user=str(input('Enter values/nums/characters(sep by comma): '))
val=user.split(',')
uni(val)
