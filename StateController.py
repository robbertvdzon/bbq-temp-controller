from State import *

class StateController:
    _state = State()

    def __init__(self):
        pass

    def getState(self):
        return self._state

    def updateState(self, state):
        self._state = state



