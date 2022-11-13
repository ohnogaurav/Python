add=0
count=0
loop_variable='y'
while loop_variable=='y' or loop_variable=="Y":
    a=int(input('enter a number :- '))
    loop_variable=input('do you want to enter more numbers? (y/n):- ')
    add+=a
    count+=1
print('the avg of the entered list is ',(add/count))
