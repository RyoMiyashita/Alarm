import RPi.GPIO as GPIO
from datetime import datetime

import SevenSegment

SevenSegmentClass = SevenSegment.SevenSegment()

hour = datetime.now().hour
minute = datetime.now().minute
microsecond = datetime.now().microsecond

try:
    while 1:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        microsecond = now.microsecond
        num1 = hour / 10 % 10
        num2 = hour % 10
        num3 = minute / 10 % 10
        num4 = minute % 10

        if microsecond < 500000:
            SevenSegmentClass.disp4Num (num1, num2, num3, num4, True)
        else:
            SevenSegmentClass.disp4Num (num1, num2, num3, num4, False)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
