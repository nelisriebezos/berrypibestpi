import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse text" )

def pulse( pin_nr, high_time, low_time ):
   """
   Geef een puls op de pin:
   Maak de pin pin_nr hoog, wacht high_time,
   maak de pin laag, en wacht nog low_time
   # copieer hier je pulse implementatie
   """
   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(low_time)

def morse( pin_nr, dot_length, text ):
   """
   Laat de text horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: spatie, streepje, punt.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   for dot in text:
      if dot == '.':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse(pin_nr, dot_length, text)

      if dot == '-':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse(pin_nr, dot_length, text)

      if dot == ' ':
         time.sleep((dot_length * 7))
         text = text[1:]
         return morse(pin_nr, dot_length, text)

def morse_text( pin_nr, dot_length, text ):
   """
   Laat de string s horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: lowercase letters, spatie.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """

   text = text.lower()

   for dot in text:
      if dot == 'a':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'b':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'c':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'd':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'e':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'f':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'g':
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'h':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'i':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'j':
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
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'k':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'l':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
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
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'm':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'n':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'o':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'p':
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'q':
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
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'r':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 's':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 't':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'u':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'v':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'w':
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'x':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'y':
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep((dot_length * 3))
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
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
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)
      if dot == 'z':
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
         GPIO.output(pin_nr, GPIO.HIGH)
         time.sleep(dot_length)
         GPIO.output(pin_nr, GPIO.LOW)
         time.sleep(dot_length)
         text = text[1:]
         return morse_text(pin_nr, dot_length, text)

led = 18
GPIO.setup( led, GPIO.OUT )
morse_text( led, 0.2, "Hello world" )
