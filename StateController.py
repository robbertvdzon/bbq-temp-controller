from State import *

class StateController:
    _state = State()
    _stateListeners = [] # type: StateListener

    def __init__(self):
        pass

    def getState(self):
        return self._state

    def updateState(self, state):
        if (not self._state == state):
            self._state = state
            for listener in self._stateListeners:
                listener.stateChanged(state)

    def addStateListener(self, listener):
        self._stateListeners.append(listener)



