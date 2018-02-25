import RPi.GPIO as GPIO
import subprocess
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 11

currentdir = os.path.dirname(os.path.abspath(__file__))

cmd = "mpg321 -l 0 " + currentdir + "/alerm1.mp3 &> /dev/null"

subprocess.Popen(cmd, shell=True)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)
