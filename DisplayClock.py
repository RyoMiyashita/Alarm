from datetime import datetime
from pytz import timezone

import SevenSegment

SevenSegmentClass = SevenSegment.SevenSegment()

jp = timezone('Asia/Tokyo')

try:
    while 1:
        now = datetime.now(jp)
        hour = now.hour
        minute = now.minute
        microsecond = now.microsecond
        num1 = int(hour / 10) % 10
        num2 = hour % 10
        num3 = int(minute / 10) % 10
        num4 = minute % 10

        if microsecond < 500000:
            SevenSegmentClass.disp4Num (num1, num2, num3, num4, True)
        else:
            SevenSegmentClass.disp4Num (num1, num2, num3, num4, False)

except KeyboardInterrupt:
    SevenSegmentClass.clear7seg()
    pass
