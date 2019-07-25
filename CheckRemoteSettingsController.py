import threading
import urllib2
import copy

class CheckRemoteSettingsController():
    _stateController = {}

    def __init__(self, stateController):
        self._stateController = stateController
        threading.Timer(2, self.onTimer).start()

    def onTimer(self):
        threading.Timer(10, self.onTimer).start()

        try:
            remoteTemp = urllib2.urlopen("https://mysmoker.api.vdzon.com/gettemp").read()
            if (remoteTemp!='-1'):
                newTempSet = int(remoteTemp)
                oldState = self._stateController.getState()
                newState = copy.copy(oldState)
                newState.bbqTempSet = newTempSet
                self._stateController.updateState(newState)
        except:
            print("Error during remote call")




