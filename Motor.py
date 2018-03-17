import RPi.GPIO as GPIO
from StateListener import *
from time import *
import time,threading



class Motor(StateListener):
    DIRECTION_OPEN = GPIO.HIGH
    DIRECTION_CLOSE = GPIO.LOW
    FULL_TIME = 3
    CLOSE_TO_HALF_TIME = 1
    OPEN_TO_HALF_TIME = 0.6
    STATE_CLOSED = 0
    STATE_HALF = 1
    STATE_OPEN = 2
    lastState = STATE_CLOSED
    requestedState = STATE_CLOSED # make sure that first time the valve is closed
    busy = False

    # KlepSensorPinOpen = 22
    # KlepSensorPinClosed = 27


    def __init__(self, stateController):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(12, GPIO.OUT) # aan / uit
        GPIO.setup(17, GPIO.OUT) # richting
        GPIO.output(12, GPIO.HIGH)

        # close valve
        self.busy = True
        self.close(self.FULL_TIME)

        stateController.addStateListener(self)
        threading.Timer(1, self.onTimer).start()


    def onTimer(self):
        threading.Timer(1, self.onTimer).start()
        if (self.busy):
            # is busy
            return
        if (self.lastState == self.requestedState):
            # nothing to do
            return

        if (self.lastState==self.STATE_CLOSED and self.requestedState==self.STATE_OPEN):
            self.open(self.FULL_TIME)
        if (self.lastState==self.STATE_CLOSED and self.requestedState==self.STATE_HALF):
            self.open(self.CLOSE_TO_HALF_TIME)
        if (self.lastState==self.STATE_HALF and self.requestedState==self.STATE_CLOSED):
            self.close(self.FULL_TIME)
        if (self.lastState==self.STATE_HALF and self.requestedState==self.STATE_OPEN):
            self.open(self.FULL_TIME)
        if (self.lastState==self.STATE_OPEN and self.requestedState==self.STATE_CLOSED):
            self.close(self.FULL_TIME)
        if (self.lastState==self.STATE_OPEN and self.requestedState==self.STATE_HALF):
            self.close(self.OPEN_TO_HALF_TIME)

        self.lastState = self.requestedState

    def open(self, time):
        self.direction(self.DIRECTION_OPEN)
        self.motorOn()
        threading.Timer(time, self.motorOff).start()

    def close(self, time):
        self.direction(self.DIRECTION_CLOSE)
        self.motorOn()
        threading.Timer(time, self.motorOff).start()

    def motorOn(self):
        GPIO.output(12, GPIO.HIGH)

    def motorOff(self):
        GPIO.output(12, GPIO.LOW)
        self.busy = False

    def direction(self, direction):
        GPIO.output(17, direction)

    def stateChanged(self, state):
        if (state.airflowPerc<10):
            self.requestedState = self.STATE_CLOSED
        if (state.airflowPerc>=10 and state.airflowPerc<20):
            self.requestedState = self.STATE_HALF
        if (state.airflowPerc>=20):
            self.requestedState = self.STATE_OPEN


    # def initKlepSensor(self):
    #     print "Klep sensor init"
    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setup(self.KlepSensorPinOpen, GPIO.IN) # pull-ups are too weak, they introduce noise
    #     GPIO.setup(self.KlepSensorPinClosed, GPIO.IN)
    #     GPIO.add_event_detect(self.KlepSensorPinOpen, GPIO.RISING, callback=self.klepOpenDetected, bouncetime=500) # bouncetime in mSec
    #     GPIO.add_event_detect(self.KlepSensorPinClosed, GPIO.RISING, callback=self.klepClosedDetected, bouncetime=500) # bouncetime in mSec
    #     return
    #
    #
    # def klepOpenDetected(self,param):
    #     p2 = GPIO.input(27)
    #     if (p2==1):
    #         print "open:"
    #     return
    #
    # def klepClosedDetected(self,param):
    #     p1 = GPIO.input(22)
    #     if (p1==1):
    #         print "closed:"
    #     return