a=int(input('Enter first side of traingle :- '))
b=int(input('Enter second side of traingle :- '))
c=int(input('Enter third side of traingle :- '))
if a==b and b==c and c==a :
    print('equilateral traingle')
elif a==b and b!=c and c!=a:
    print('isoceles traingle')
else:
    print('scalen traingle')
