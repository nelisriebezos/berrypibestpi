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
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.on()
    sleep(3)
    led.off()
    sleep(1)



   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(dot_length)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(dot_length)

   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep((dot_length * 3))
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(dot_length)

   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep((dot_length * 3))
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(dot_length)

   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(dot_length)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(dot_length)

   time.sleep((dot_length * 7))