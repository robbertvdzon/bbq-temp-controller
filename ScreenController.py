from datetime import datetime
from InputListener import *

class ScreenController(InputListener):
    _display = {}
    _stateController = {}

    def __init__(self, display, encoder, stateController):
        self._display = display
        self._stateController = stateController
        self._display.clearDisplay()
        encoder.addInputListener(self)

    def buttonTimeout(self):
        print "timeout in screen"

    def buttonUp(self):
        print "up in screen"

    def buttonDown(self):
        print "down in screen"

    def buttonPressed(self):
        print "pressed in screen"

    def drawScreen(self):
        state = self._stateController.getState()
        time = datetime.now().time()
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # ip = s.getsockname()[0]
        # s.close()

        self._display.display("BBQ  : "+str(state.bbqTemp)+" ("+str(state.bbqTempSet)+")", 1)
        self._display.display("Vlees: "+str(state.meatTemp)+" ("+str(state.meatTempSet)+")", 2)
        # self.display.display(ip,3)
        self._display.display(str(time)[:8], 4)


