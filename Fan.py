import RPi.GPIO as GPIO
from StateListener import *
from time import *
import time,threading



class Fan(StateListener):
    cycleTime = 10
    onTime = 0
    offTime = cycleTime


    def __init__(self, stateController):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(5, GPIO.OUT) # FAN

        stateController.addStateListener(self)
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        if (self.onTime==0):
            self.fanOff()
            threading.Timer(self.cycleTime, self.onTimer).start()
        else:
            self.fanOn()
            threading.Timer(self.onTime, self.closeFan).start()

    def closeFan(self):
        self.fanOff()
        threading.Timer(self.offTime, self.onTimer).start()

    def fanOff(self):
        GPIO.output(5, GPIO.LOW)

    def fanOn(self):
        GPIO.output(5, GPIO.HIGH)

    def stateChanged(self, state):
        self.airflowPerc = state.airflowPerc
        self.onTime = self.cycleTime*self.airflowPerc/100.0
        self.offTime = self.cycleTime - self.onTime
