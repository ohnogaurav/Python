
# run this program paste your victim's ip adress and find their location , woohoo ! your a hacker now :)
#connect your pc to internet first !!
import os
import urllib.request
import json

while True:
    ip=input('Whats your target IP :  ')
    url='http://ip-api.com/json/'
    response = urllib.request.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print('IP : ' + values['query'])
    print('City : ' + values['city'])
    print('ISP : ' + values['isp'])
    print('Country : ' + values['country'])
    print('Region : ' + values['region'])
    print('Time zone : ' + values['timezone'])
    break
