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
        airflowPerc = self._calcAirflow()
        self._updateState(airflowPerc)

    def _calcAirflow(self):
        state = self.stateController.getState()
        if state.forceCloseAirflow:
            return 0
        return state.bbqTempSet

    def _updateState(self, airflowPerc):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.airflowPerc = airflowPerc
        self.stateController.updateState(newState)

