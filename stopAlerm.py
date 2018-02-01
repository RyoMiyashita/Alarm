import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 11
SW = 9

waitSec = 60
intervalSec = 0.25

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN)
for value in range(0, int(waitSec/intervalSec)):
    SWIn = GPIO.input(SW)
    if SWIn == 1:
        break
    sleep(intervalSec)

subprocess.call("killall -s SIGKILL mpg321", shell=True)
GPIO.output(LED, 0)
