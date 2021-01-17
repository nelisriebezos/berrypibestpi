import time
import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

# 4, 18, 17, 27, 22
led = 22
GPIO.setup( led, GPIO.OUT )

while True:
   GPIO.output( led, GPIO.HIGH )
   time.sleep( 0.5 )
   GPIO.output( led, GPIO.LOW )
   time.sleep( 0.5 )
