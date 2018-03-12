import threading, copy
from State import *
import Adafruit_ADS1x15

class TemperatureController:
    stateController = {}
    _adc = Adafruit_ADS1x15.ADS1015()

    def __init__(self, stateController):
        print "init"
        self.stateController = stateController
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        threading.Timer(1, self.onTimer).start()
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.bbqTemp = self._adc.read_adc(3, gain=1)
        newState.meatTemp = self._adc.read_adc(2, gain=1)
        self.stateController.updateState(newState)


