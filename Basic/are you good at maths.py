import random
operators=['+','-','*']
error,score=0,0
print('Are you good at doing maths ? well lets check :)')
print('rule: +4 marks for correct answer & -2 marks for incorrect answer')

for i in range(5):
    print('-'*50)
    n1=random.randint(1,100)
    n2=random.randint(1,100)
    i=random.randrange(0,3)
    op=operators[i]
    result=0

    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1 * n2
    print(n1,op,n2,'=')
    ask=int(input())
    if ask == result: score+=4

    else: score-=2

print('-'*50)
print('##----------[YOU SCORED:',str(score)+']----------##')
