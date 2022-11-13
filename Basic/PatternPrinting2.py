'''
output
A P Q R
A B Q R
A B C R
A B C D
'''
str1='ABCD'
str2='PQR'
j=0
for i in range (1,5):
    print(str1[:+i],str2[j:],sep='')
    j+=1
