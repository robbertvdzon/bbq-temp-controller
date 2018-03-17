import threading, copy
from State import *
import Adafruit_ADS1x15
from StateListener import *

class AirflowController(StateListener):
    stateController = {}
    lastForceCloseAirflow = False

    def __init__(self, stateController):
        self.stateController = stateController
        stateController.addStateListener(self)
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        threading.Timer(20, self.onTimer).start()
        airflowPerc = self._calcAirflow()
        self._updateState(airflowPerc)

    def _calcAirflow(self):
        state = self.stateController.getState()
        if state.forceCloseAirflow:
            return 0
        return state.bbqTempSet

    def stateChanged(self, state):
        if (self.lastForceCloseAirflow!=state.forceCloseAirflow):
            self.onTimer()
        self.lastForceCloseAirflow = state.forceCloseAirflow


    def _updateState(self, airflowPerc):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.airflowPerc = airflowPerc
        self.stateController.updateState(newState)

