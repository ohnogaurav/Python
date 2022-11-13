from time import sleep
from pygame import mixer
a=int(input('set a timer in seconds:- '))
b=int(input('set a time duration for music:- '))
print('Alarm will be trigerred after',a,"secs")
print('It will be trigerred for',b,"secs")

sleep(a)
mixer.init()
mixer.music.load('music.wav')
mixer.music.play()
sleep(b)
mixer.music.stop()


print('total time taken:- ',a+b,'secs')
