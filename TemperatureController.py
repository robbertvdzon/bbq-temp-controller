import threading
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
        state = self.stateController.getState()
        newBbqTemp = self._adc.read_adc(3, gain=1)
        newMeatTemp = self._adc.read_adc(2, gain=1)
        state.bbqTemp = newBbqTemp
        state.meatTemp = newMeatTemp
        self.stateController.updateState(state)


