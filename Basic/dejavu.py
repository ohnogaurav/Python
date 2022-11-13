a=list(input())
a.sort()
length=len(a)
unq=[]
dup=[]
count=i=0
while i<length:
    count=1
    element=a[i]
    if element not in unq and element not in dup:
        i+=1
        for j in range (i,length):
            if element == a[j]:
                count+=1
        else:
            #print(count,element,end=" ",sep="")
            if count==1:
                unq.append(element)
            else:
                dup.append(element)
    else:
        i+=1

t=len(dup)
if t!=0:
    print("dejavu")
else:
    print("unique")
