str=input('Enter a string: ')
lenght=len(str)
empstr=''
for i in range(0,lenght,2):
    empstr+=str[i]
    if i<(lenght-1):
        empstr+=str[i+1].upper()
print(empstr)
