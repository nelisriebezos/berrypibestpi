import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

led = 18
switch = 23
knop_status = False

GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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
    if GPIO.input(switch) and knop_status == False:
        p = start()  # roep functie aan om het programma te starten
        GPIO.output(led, GPIO.HIGH)
        knop_status = True
        time.sleep(0.05)
    elif GPIO.input(switch) and knop_status == True:
        stop(p)  # roep functie aan om het programma te sluiten
        GPIO.output(led, GPIO.LOW)
        knop_status = False
        time.sleep(0.05)
    time.sleep(0.1)