while True:          #on first go
    a=list(input()) #instagram
    a.sort()        #aagimnrst
    length=len(a)   #9
    count=i=0       #i=0
    unq=[]
    dup=[]

    while i < length:#0<9
        element=a[i]#element=a
        count=1     #supposing its occuring for the first time
        if element not in unq and element not in dup :#only run if both of the list has no element
            i+=1    #i=1
            for j in range (i,length):#(1,6) ie upto 5
                if element == a[j]: #a==a?? yes !
                    count+=1        #count=2
            else:                   #this block  will run after complition of if loop of for loop part
                print(count,element,end=' ',sep="")#2a
                if count==1:        #nope !
                    unq.append(element)
                else:               #this will run
                    dup.append(element) #a appended to dup list
        else:
            i+=1
    print()
