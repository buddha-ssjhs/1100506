#PIR使用範例
from machine import Pin
from utime import sleep

PIR = Pin(2, Pin.IN, Pin.PULL_DOWN)

i=0
while True:
    print(i,PIR.value())
    sleep(1)
    i+=1