import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

knop_led_gpio = 18
knop_gpio = 23
knop_status = False

GPIO.setup(knop_led_gpio, GPIO.OUT)
GPIO.setup(knop_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def start():
    try:
        return subprocess.Popen(['python', 'main.py'])
    except:
        print('Program could not be opened.')


def stop(p):
    try:
        p.terminate()
    except:
        print('Program could not be closed.')


while True:
    if GPIO.input(knop_gpio) and knop_status == False:
        p = start()  # roep functie aan om het programma te starten
        GPIO.output(knop_led_gpio, GPIO.HIGH)
        knop_status = True
        time.sleep(0.05)
    elif GPIO.input(knop_gpio) and knop_status == True:
        stop(p)  # roep functie aan om het programma te sluiten
        GPIO.output(knop_led_gpio, GPIO.LOW)
        knop_status = False
        time.sleep(0.05)
    time.sleep(0.1)