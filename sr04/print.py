import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

trig = 20
echo = 21

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """

   GPIO.output(trig_pin, GPIO.HIGH)
   time.sleep(0.3)
   GPIO.output(trig_pin, GPIO.LOW)

   while GPIO.input(echo_pin) == 0:
      pass
   start = time.time()

   while GPIO.input(echo_pin) == 1:
      pass
   end = time.time()

   distance = ((end - start)/58.0*1000000)
   return distance

while True:
   print(sr04(trig, echo))
   time.sleep( 0.5 )
