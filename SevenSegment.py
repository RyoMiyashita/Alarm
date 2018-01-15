import RPi.GPIO as GPIO

class SevenSegment :
    sevenSegmentsGPIO = [2, 3, 4, 14]
    numGPIO = {
        "A" : 24,
        "B" : 25,
        "C" : 23,
        "D" : 17,
        "E" : 18,
        "F" : 22,
        "G" : 10,
        "DP" : 27,
    }

    def __init__(self) :
        self.sevenSegmentsGPIO = [2, 3, 4, 14]
        self.numGPIO = {
            "A" : 24,
            "B" : 25,
            "C" : 23,
            "D" : 17,
            "E" : 18,
            "F" : 22,
            "G" : 10,
            "DP" : 27,
        }
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sevenSegmentsGPIO, GPIO.OUT)
        GPIO.setup(list(self.numGPIO.values()), GPIO.OUT)


    def aDispNum(self, ch = 0, num = 0) :
        if ch > 3 :
            ch = 0

        for seg in self.sevenSegmentsGPIO :
            GPIO.output(seg, 0)

        GPIO.output(self.sevenSegmentsGPIO[ch], 1)
        GPIO.output(list(self.numGPIO.values()), 1)

        if num == 0 :
            for gpio in "A", "B", "C", "D", "E", "F" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 1 :
            for gpio in "B", "C" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 2 :
            for gpio in "A", "B", "D", "E", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 3 :
            for gpio in "A", "B", "C", "D", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 4 :
            for gpio in "B", "C", "F", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 5 :
            for gpio in "A", "C", "D", "F", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 6 :
            for gpio in "A", "C", "D", "E", "F", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 7 :
            for gpio in "A", "B", "C", "F" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 8 :
            for gpio in "A", "B", "C", "D", "E", "F", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        elif num == 9 :
            for gpio in "A", "B", "C", "F", "G" :
                GPIO.output(self.numGPIO[gpio], 0)

        else :
            GPIO.output(self.numGPIO["DP"], 0)
