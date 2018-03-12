from display import *
import RPi.GPIO as GPIO
from time import *
import time,threading

class Encoder:
    Enc_A = 19
    Enc_B = 13
    inputListeners = [] # type: InputListener
    lastMillis = 0
    sleepMode = True

    def __init__(self):
        self.initEncoder()
        self.initKnopSensor()
        threading.Timer(1, self.onTimer).start()

    def addInputListener(self, listener):
        self.inputListeners.append(listener)

    def initEncoder(self):
        global counter
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.setup(self.Enc_B, GPIO.IN)
        GPIO.add_event_detect(self.Enc_A, GPIO.RISING, callback=self.rotation_decode, bouncetime=2) # bouncetime in mSec
        return

    def initKnopSensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.add_event_detect(6, GPIO.RISING, callback=self.knopPressedDetected, bouncetime=200) # bouncetime in mSec
        return


    def knopPressedDetected(self, param):
        self.updateTimeout()
        for listener in self.inputListeners:
            listener.buttonPressed()

    def rotation_decode(self, Enc_A):
        self.updateTimeout()
        sleep(0.002) # extra 2 mSec de-bounce time
        Switch_A = GPIO.input(self.Enc_A)
        Switch_B = GPIO.input(self.Enc_B)
        if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
            for listener in self.inputListeners:
                listener.buttonDown()
            while Switch_B == 0:
                Switch_B = GPIO.input(self.Enc_B)
            # now wait for B to drop to end the click cycle
            while Switch_B == 1:
                Switch_B = GPIO.input(self.Enc_B)
            return
        elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
            for listener in self.inputListeners:
                listener.buttonUp()
            while Switch_A == 1:
                Switch_A = GPIO.input(Enc_A)
            return
        else: # discard all other combinations
            return
            # end code voor encoder

    def updateTimeout(self):
        self.lastMillis = time.time()*1000.0
        self.sleepMode = False

    def onTimer(self):
        threading.Timer(1, self.onTimer).start()
        if self.sleepMode:
            return
        currentMillis = time.time()*1000.0
        diff = currentMillis-self.lastMillis

        if (diff>5*1000):
            self.sleepMode = True
            for listener in self.inputListeners:
                listener.buttonTimeout()
