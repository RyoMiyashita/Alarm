import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 11

subprocess.call("mpg321 -l 0 alerm1.mp3 &> /dev/null", shell=True)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)
