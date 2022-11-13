'''
WAP to count number of consonants present in a message
'''
def cc(str):
    str.lower()
    count=0
    conso=['a','e','i','o','u']
    for i in str:
        if i not in conso:
            count+=1
    return count
text=input('enter a message:  ')
number=cc(text)
if number>0:
    print('There are',number,'consonants')
else:
    print('no consonants found in the given text')
