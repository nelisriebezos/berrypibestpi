# servo = 25
# GPIO.setup( servo, GPIO.OUT )
#
# ms = 1.0/1000.0
# span = 20 * ms
# duration = 2.4*ms
# print(span)
# print(duration)
#
# pulse(servo, duration, span - duration)


import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, delay1, delay2 ):
   GPIO.output(pin, GPIO.HIGH)
   time.sleep(delay1)
   GPIO.output(pin, GPIO.LOW)
   time.sleep(delay2)


def servo_pulse( pin_nr, position ):
   span = 0.02
   formule = round(((position*span) + 0.4) / 1000, 7)
   pulse(pin_nr, formule, span-formule)



servo = 25
GPIO.setup( servo, GPIO.OUT )
while True:
   for i in range( 0, 101, 1 ):
      servo_pulse( servo, i )
   for i in range( 101, 0, -1 ):
      servo_pulse( servo, i )


