import RPi.GPIO as GPIO
import time

import SevenSegment

SevenSegmentClass = SevenSegment.SevenSegment()

try:
    while 1:
        SevenSegmentClass.aDispNum(0, 0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
