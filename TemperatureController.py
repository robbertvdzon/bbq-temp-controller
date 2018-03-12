import threading, copy
from State import *
import Adafruit_ADS1x15

class TemperatureController:
    stateController = {}
    _adc = Adafruit_ADS1x15.ADS1015()

    def __init__(self, stateController):
        self.stateController = stateController
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        threading.Timer(1, self.onTimer).start()
        bbqTemp = self._adc.read_adc(3, gain=1)
        meatTemp = self._adc.read_adc(2, gain=1)
        self._updateState(bbqTemp, meatTemp)


    def _updateState(self, bbqTemp, meatTemp):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.bbqTemp = bbqTemp
        newState.meatTemp = meatTemp
        self.stateController.updateState(newState)

