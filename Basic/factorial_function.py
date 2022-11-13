def factorial(n):
    if n==0:
        return 'Factorial of 0 is 1'
    elif n>1:
        ramp=1
        while n>1:
            ramp=ramp*n
            n=n-1
        return ramp
    else:
        return 'Factorial of negative numbers does not exist'


num=int(input('Enter a Number:'))
a=factorial(num)
print(a)
