import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

servo_gpio = 25
GPIO.setup(servo_gpio, GPIO.OUT)
# spelpercentage = random.randint(1, 100)

def pulse(pin, positie, wachttijd):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(positie)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(wachttijd)


def servo_pulse(pin_nr, percentage):
    wachttijd = 0.02
    positie = round(((percentage * wachttijd) + 0.4) / 1000, 7)
    pulse(pin_nr, positie, wachttijd - positie)

while True:
    spelpercentage = random.randint(1, 100)
    servo_pulse(servo_gpio, spelpercentage)
    time.sleep(.5)