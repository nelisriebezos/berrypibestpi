import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

sensor_trigger_gpio = 20
sensor_echo_gpio = 21

GPIO.setup(sensor_trigger_gpio, GPIO.OUT)
GPIO.setup(sensor_echo_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sr04( trig_pin, echo_pin ):
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


def roepsensoraan():
    distancelijst = []

    print('lijst voor:', distancelijst)
    time.sleep(1)
    for i in range(3):
        distance = (round((sr04(sensor_trigger_gpio, sensor_echo_gpio)), 0))
        print(distance)
        distancelijst.append(distance)
        time.sleep(0.2)
    print('lijst na', distancelijst)

    print(distancelijst)

    average_distance = sum(distancelijst) / len(distancelijst)
    print(average_distance)

    if average_distance < 10:
        switch_dashboard()
    elif average_distance > 10 and average_distance > 25:
        switch_dashboard()
    else:
        switch_dashboard()

roepsensoraan()