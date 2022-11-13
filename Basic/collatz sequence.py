

def collatz(num):
    if num%2==0:
        num=num//2
        return(num)
    elif num%2==1:
        num=(3*num)+1
        return(num)

user=int(input('Enter a num: '))

while user!=1:
    print(collatz(user))
    t=collatz(user)
    user=t
input()
