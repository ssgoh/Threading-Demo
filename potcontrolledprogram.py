#Libraries
import os
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
import _thread
from machine import ADC

#setup
button = Pin(3,Pin.IN,Pin.PULL_DOWN)
status_led=Pin(2,Pin.OUT)
pot = ADC(0) # creates an ADC object using pin A0
proglist=["Blink Red   ","Blink Yellow","Blink Blue  ","Blink Green ","Blink White "]
filelist=["red.py","yellow.py","blue.py","green.py","white.py"]
spi = SPI(0, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(6), mosi=Pin(7), miso=None)
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

    
    
#functions
def button_pressed(val):
    print('button pressed')
    button.irq(handler=None)
    _thread.start_new_thread(runprog(),())
    time.sleep(.5)
    
 
def runprog():
    button.irq(trigger=machine.Pin.IRQ_RISING , handler=None)
    print('run',file)
    status_led.on()
    exec(open(file).read())
    print('end')
    _thread.exit()
    
   

  
#Program / Algorithm
status_led.off()
     
while True:
    button.irq(trigger=machine.Pin.IRQ_RISING , handler=button_pressed)
    status_led.off()
    
    global file, prog
    value = pot.read_u16() # reads the value of the potentiometer
    print(value)
    
    if 0 <= value and value <= 13000:
        prog=proglist[0]
        file=filelist[0]
    elif 13001 <= value and value <=26000:
        prog=proglist[1]
        file=filelist[1]
    elif 26001 <= value and value <= 39000:
        prog=proglist[2]
        file=filelist[2]
    elif 39001 <= value and value <=52000:
        prog=proglist[3]
        file=filelist[3]
    else:
        prog=proglist[4]
        file=filelist[4]

    tft.text((10, 60), prog, TFT.WHITE, sysfont, 1)
    tft.text((10, 80), f"Run {file}    ", TFT.WHITE, sysfont, 1)
    
     
 

"""
#Remarks
#Wiring for TFT display
spi = SPI(0, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(6), mosi=Pin(7), miso=None)
tft=TFT(spi,16,17,18)
def __init__( self, spi, aDC, aReset, aCS) :
aLoc SPI pin location is either 1 for 'X' or 2 for 'Y'.
   aDC is the DC  pin and aReset is the reset pin.
   aCS is CS pin
"""
 