

from pygame import mixer
from time import sleep


mixer.init()
mixer.music.load('mariotheme.mp3')
mixer.music.play(10)

sleep(5)

mixer.init()
mixer.music.load('die.wav')
mixer.music.play(1)

