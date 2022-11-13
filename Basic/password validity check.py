'''
password
'''
password=input('Enter your password: ')
len=len(password)
upper=lower=num=sc=0
if len>=8:
    for i in password :
        if i.isupper() :
            upper+=1
        elif i.islower() :
            lower+=1
        elif i.isdigit() :
            num+=1
        elif ord(i)> 33 and ord(i)< 127 :
            sc+=1
if num>0 and lower>0 and upper>0 and sc>0 :
    print('valid password')
else:
    print('invalid password')
