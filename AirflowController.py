import threading, copy
from State import *
import Adafruit_ADS1x15

class AirflowController:
    stateController = {}

    def __init__(self, stateController):
        self.stateController = stateController
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        threading.Timer(1, self.onTimer).start()
        (valvePercOpen, fanOn) = self._calcAirflow()
        self._updateState(valvePercOpen, fanOn)

    def _calcAirflow(self):
        state = self.stateController.getState()
        if state.forceCloseAirflow:
            return 0,False
        return state.bbqTempSet,state.bbqTempSet>30

    def _updateState(self, valvePercOpen, fanOn):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.valvePercOpen = valvePercOpen
        newState.fanOn = fanOn
        self.stateController.updateState(newState)

