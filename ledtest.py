
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )
led = LED(4)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)