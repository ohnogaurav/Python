'''
program that reads a line and a substring
and return no of occ of substring
'''
str=input('')
substr=input('')
length=len(str)
lengthsub=len(substr)

start=count=0
end=length

while True:
    position=str.find(substr,start,end)
    if position !=-1:
        count+=1
        start=position+lengthsub
    else :
        break
    if start >= length:
        break
print('no of occ of',substr,':',count)
