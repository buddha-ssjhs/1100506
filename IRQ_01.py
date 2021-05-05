#IRQ使用範例
from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
buzzer = Pin(10,  Pin.OUT)
button_2 = Pin(13, Pin.IN, Pin.PULL_DOWN) #按鈕2接上拉電阻

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
    
def IRQ(pin):
    button_2.irq(handler=None)
    print("interrupt")
    for i in range(3):
        buzzer.value(1)
        sleep(0.2)
        buzzer.value(0)
        sleep(0.2)

while True:
    button_2.irq(trigger=Pin.IRQ_RISING,handler=IRQ)
    trafficlight()
    