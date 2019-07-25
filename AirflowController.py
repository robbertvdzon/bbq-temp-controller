import threading, copy
from State import *
import Adafruit_ADS1x15
from StateListener import *
from AirflowCalculator import *
import datetime

class AirflowController(StateListener):
    stateController = {}
    lastForceCloseAirflow = False
    lastForceFullAirflow = False
    airflowCalculator = AirflowCalculator()
    lastBbqTemp = 0

    def __init__(self, stateController):
        self.stateController = stateController
        stateController.addStateListener(self)
        threading.Timer(1, self.onAirflowTimer).start()

    def onAirflowTimer(self):
        threading.Timer(30, self.onAirflowTimer).start()
        airflowPerc = self._calcAirflow()
        self._updateState(airflowPerc)

    def _calcAirflow(self):
        state = self.stateController.getState()
#        if state.forceFullAirflow:
#            return 100
#        if state.forceCloseAirflow:
#            return 0
        currentTemp = state.bbqTemp
        lastBbqTemp = self.lastBbqTemp
        self.lastBbqTemp = state.bbqTemp
        result = self.airflowCalculator.calcAirflow(state.bbqTempSet, currentTemp, lastBbqTemp, state.airflowPerc)
        print "%s set: %s  current:%s  last: %s currentflow: %s newflow: %s" % (datetime.datetime.now(), state.bbqTempSet, currentTemp, lastBbqTemp, state.airflowPerc, result)
        return result

    def stateChanged(self, state):
       # if (self.lastForceCloseAirflow!=state.forceCloseAirflow):
       #     self.onTimer()
       # if (self.lastForceFullAirflow!=state.forceFullAirflow):
       #     self.onTimer()
        self.lastForceCloseAirflow = state.forceCloseAirflow
        self.lastForceFullAirflow = state.forceFullAirflow


    def _updateState(self, airflowPerc):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.airflowPerc = airflowPerc
        self.stateController.updateState(newState)

