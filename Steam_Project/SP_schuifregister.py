import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

SR_shift_gpio = 5
SR_latch_gpio = 6
SR_data_gpio = 13

GPIO.setup(SR_shift_gpio, GPIO.OUT)
GPIO.setup(SR_latch_gpio, GPIO.OUT)
GPIO.setup(SR_data_gpio, GPIO.OUT)


led = {
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 16,
    6: 32,
    7: 64,
    8: 128
}


def activateOne(shift_clock_pin, latch_clock_pin, data_pin, value):
    value = led[value]
    for i in range(8):
        if value % 2 == 1:
            GPIO.output(data_pin, GPIO.HIGH)
        else:
            GPIO.output(data_pin, GPIO.LOW)
        value = value // 2

        GPIO.output(shift_clock_pin, GPIO.HIGH)
        GPIO.output(shift_clock_pin, GPIO.LOW)

    GPIO.output(latch_clock_pin, GPIO.HIGH)
    GPIO.output(latch_clock_pin, GPIO.LOW)


def activateMultiple(shift_clock_pin, latch_clock_pin, data_pin, values):
    lst = [0 for i in range(8)]
    for v in values:
        if v < 9 and v > 0:
            lst[v-1] = v

    for i in lst:
        if i >= 1:
            GPIO.output(data_pin, GPIO.HIGH)
        else:
            GPIO.output(data_pin, GPIO.LOW)

        GPIO.output(shift_clock_pin, GPIO.HIGH)
        GPIO.output(shift_clock_pin, GPIO.LOW)

    GPIO.output(latch_clock_pin, GPIO.HIGH)
    GPIO.output(latch_clock_pin, GPIO.LOW)


def pattern(inp):
    if inp % 2 == 0:
        return [i for i in range(2, 9, 2)]
    else:
        return [i for i in range(1, 9, 2)]


delay = 0.2

activateMultiple(SR_shift_gpio, SR_latch_gpio, SR_data_gpio, [0, 0, 0, 0, 0, 0, 0, 0])
# while True:
#     for i in range(1, 4, 1):
#         activateMultiple(shift_clock_pin, latch_clock_pin,
#                          data_pin, pattern(i))
#         time.sleep(delay)
#
#     for i in range(1, 9, 1):
#         activateOne(shift_clock_pin, latch_clock_pin, data_pin, i)
#         time.sleep(delay)
#
#     for i in range(4, 0, -1):
#         activateMultiple(shift_clock_pin, latch_clock_pin,
#                          data_pin, pattern(i))
#         time.sleep(delay)
#
#     for i in range(8, 0, -1):
#         activateOne(shift_clock_pin, latch_clock_pin, data_pin, i)
#         time.sleep(delay)
