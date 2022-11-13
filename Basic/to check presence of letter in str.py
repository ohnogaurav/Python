'''
WAP to check the presence of any letter in the given text.
'''

def pcheck(t,l):
    global count
    count=0
    if l in t:
        count+=1
    return count

text=input('enter text here: ')
letter=input('enter letter here to check its presence: ')
count=0

pcheck(text,letter)

if count>0:
    print(letter,"is present")
elif count==0:
    print(letter,"is not present")
