import threading, copy, pickle

class StorageController():
    _stateController = {}

    def __init__(self, stateController):
        self._stateController = stateController
        self._loadStateFromDisk()
        threading.Timer(10, self.onTimer).start()

    def _loadStateFromDisk(self):
        try:
            with open('state.pkl', 'rb') as input:
                state = pickle.load(input)
                self._stateController.updateState(state)
        except:
            pass


    def onTimer(self):
        threading.Timer(10, self.onTimer).start()
        state = self._stateController.getState()
        with open('state.pkl', 'wb') as output:
            pickle.dump(state, output, pickle.HIGHEST_PROTOCOL)
