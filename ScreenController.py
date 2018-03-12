from datetime import datetime
from InputListener import *
from StateListener import *
from Display import *
import threading, copy

class ScreenController(InputListener, StateListener):
    _display = {}
    _stateController = {}
    _currentState = {}
    _lock = threading.Lock()
    _screenNr = 0

    def __init__(self, display, encoder, stateController):
        self._display = display
        self._stateController = stateController
        stateController.addStateListener(self)
        self._display.clearDisplay()
        encoder.addInputListener(self)

    def stateChanged(self, state):
        self._currentState = state
        self.drawScreen()

    def buttonTimeout(self):
        self._screenNr = 0
        self.drawScreenMenu()

    def buttonUp(self):
        if (self._screenNr==1):
            oldState = self._stateController.getState()
            newState = copy.copy(oldState)
            newState.bbqTempSet = newState.bbqTempSet+1
            self._stateController.updateState(newState)
        if (self._screenNr==2):
            oldState = self._stateController.getState()
            newState = copy.copy(oldState)
            newState.meatTempSet = newState.meatTempSet+1
            self._stateController.updateState(newState)

    def buttonDown(self):
        if (self._screenNr==1):
            oldState = self._stateController.getState()
            newState = copy.copy(oldState)
            newState.bbqTempSet = newState.bbqTempSet-1
            self._stateController.updateState(newState)
        if (self._screenNr==2):
            oldState = self._stateController.getState()
            newState = copy.copy(oldState)
            newState.meatTempSet = newState.meatTempSet-1
            self._stateController.updateState(newState)

    def buttonPressed(self):
        self._screenNr = self._screenNr+1
        if (self._screenNr>3):
            self._screenNr = 0
        self.drawScreenMenu()

    def drawScreen(self):
        self._lock.acquire()
        try:
            self._drawScreen()
        finally:
            self._lock.release() # release lock, no matter what

    def drawScreenBbqTemp(self):
        self._lock.acquire()
        try:
            self._drawScreenBbqTemp()
        finally:
            self._lock.release() # release lock, no matter what

    def drawScreenMeatTemp(self):
        self._lock.acquire()
        try:
            self._drawScreenMeatTemp()
        finally:
            self._lock.release() # release lock, no matter what

    def drawScreenMenu(self):
        self._lock.acquire()
        try:
            self._drawScreenMenu()
        finally:
            self._lock.release() # release lock, no matter what

    def _drawScreen(self):
        self._drawScreenBbqTemp()
        self._drawScreenMeatTemp()
        self._drawScreenMenu()
        # time = datetime.now().time()
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # ip = s.getsockname()[0]
        # s.close()



    def _drawScreenBbqTemp(self):
        state = self._currentState
        self._display.display("BBQ  : "+str(state.bbqTemp)+" ("+str(state.bbqTempSet)+")", 1)

    def _drawScreenMeatTemp(self):
        state = self._currentState
        self._display.display("Vlees: "+str(state.meatTemp)+" ("+str(state.meatTempSet)+")", 2)

    def _drawScreenMenu(self):
        state = self._currentState
        if (self._screenNr == 0 ):
            self._display.display("Running", 4)
        if (self._screenNr == 1 ):
            self._display.display("Set bbq temp", 4)
        if (self._screenNr == 2 ):
            self._display.display("Set meat temp", 4)
        if (self._screenNr == 3 ):
            self._display.display(self._currentState.ipadress, 4)
