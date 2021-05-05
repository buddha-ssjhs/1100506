#蜂鳴器使用範例
from machine import Pin
from utime import sleep

buzzer = Pin(10, Pin.OUT)

for i in range(3):
    buzzer.value(1)
    sleep(0.5)
    buzzer.value(0)
    sleep(0.5)
    