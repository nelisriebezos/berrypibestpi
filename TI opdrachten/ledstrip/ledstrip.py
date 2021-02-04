import time
import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM ) 
GPIO.setwarnings( 0 )

print( "neopixels walk" )

clock_pin = 19
data_pin = 26

GPIO.setup( clock_pin, GPIO.OUT )
GPIO.setup( data_pin, GPIO.OUT )

def apa102_send_bytes( clock_pin, data_pin, bytes ):
    for byte in bytes:
        for bitnr in range(7,-1,-1):
            checkbit = 1<<bitnr
            if byte & checkbit != 0:
                GPIO.output(data_pin, GPIO.HIGH)
            else:
                GPIO.output(data_pin, GPIO.LOW)
            GPIO.output(clock_pin, GPIO.HIGH)
            GPIO.output(clock_pin, GPIO.LOW)


def apa102( clock_pin, data_pin, colors ):
    apa102_send_bytes(clock_pin, data_pin, [0,0,0,0])
    for i in colors:
        apa102_send_bytes(clock_pin, data_pin, [255, (*i)])
    apa102_send_bytes(clock_pin, data_pin, [255,255,255,255])

blue = [ 8, 0, 0 ]
green = [ 0, 255, 0 ]
red = [ 0, 0, 255 ]

def colors( x, n, on, off ):
   result = []
   for i in range( 0, n ):
      if i == x:
           result.append( on )
      else:
           result.append( off )
   print(result)
   return result           

def walk( clock_pin, data_pin, delay, n = 8 ):
   while True:
      for x in range( 0, n ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
      for x in range( n - 2, 0, -1 ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
         
walk( clock_pin, data_pin, 0.03 )         
