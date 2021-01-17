import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch = 23

GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

BS = False

while True:
   if GPIO.input(switch) == 1:
      print("switch is pressed")
      if BS == False:
         GPIO.output(led, True)
         BS = True
         time.sleep(0.5)
      else:
         GPIO.output(led, False)
         BS = False
         time.sleep(0.5)
