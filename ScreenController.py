from datetime import datetime
from InputListener import *
from StateListener import *
import threading

class ScreenController(InputListener, StateListener):
    _display = {}
    _stateController = {}
    _currentState = {}
    _lock = threading.Lock()

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
        print "timeout in screen"

    def buttonUp(self):
        self.drawScreen()
        print "up in screen"

    def buttonDown(self):
        self.drawScreen()
        print "down in screen"

    def buttonPressed(self):
        self.drawScreen()
        print "pressed in screen"

    def drawScreen(self):
        self._lock.acquire()
        try:
            self._drawScreen()
        finally:
            self._lock.release() # release lock, no matter what

    def _drawScreen(self):
        state = self._currentState
        time = datetime.now().time()
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # ip = s.getsockname()[0]
        # s.close()

        self._display.display("BBQ  : "+str(state.bbqTemp)+" ("+str(state.bbqTempSet)+")", 1)
        self._display.display("Vlees: "+str(state.meatTemp)+" ("+str(state.meatTempSet)+")", 2)
        # self.display.display(ip,3)
        self._display.display(str(time)[:8], 4)


