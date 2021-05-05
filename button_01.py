#按鈕使用範例
from machine import Pin
from utime import sleep

led_red = Pin(18, Pin.OUT)
led_amber = Pin(17, Pin.OUT)
led_green = Pin(16, Pin.OUT)
button_1 = Pin(15, Pin.IN, Pin.PULL_UP) #本例使用上拉電阻,輸入pin號為15,另一端接GND

while True:
    if button_1.value() == 0:
        for i in range(3):
            led_amber.value(1)
            sleep(0.5)
            led_amber.value(0)
            sleep(0.5)
