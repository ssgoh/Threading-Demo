
from machine import Pin
from time import sleep
white=Pin(5,Pin.OUT)
green=Pin(4,Pin.OUT)
blue=Pin(10,Pin.OUT)
yellow=Pin(28,Pin.OUT)
red=Pin(27,Pin.OUT)

def init():
    white.off()
    green.off()
    blue.off()
    yellow.off()
    red.off()
    


for x in range(5):
    print('green',x)
    init()
    sleep(1)
    green.on()
    sleep(1)
green.off()

