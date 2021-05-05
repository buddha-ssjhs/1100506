#使用IF判斷式
from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10, Pin.OUT)
PIR = Pin(2, Pin.IN, Pin.PULL_DOWN)#ACC端需接5V電源

def trafficlight():
    led_red.value(1)
    sleep(2)
    led_red.value(0)
    led_amber.value(1)
    sleep(2)
    led_amber.value(0)
    led_green.value(1)
    sleep(2)
    led_green.value(0)
    led_amber.value(1)
    sleep(2)
    led_amber.value(0)

def pedestrianfirst():
    print("行人優先")
    led_red.value(1)
    led_amber.value(0)
    led_green.value(0)
    for i in range(5):
        buzzer.value(1)
        sleep(0.2)
        buzzer.value(0)
        sleep(0.2)
    led_red.value(0)
   
while True:
    trafficlight()
    if PIR.value() == 1:
        pedestrianfirst()