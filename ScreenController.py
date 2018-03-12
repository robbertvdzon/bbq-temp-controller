from datetime import datetime
from InputListener import *

class ScreenController(InputListener):
    display = {}

    def __init__(self, display, encoder):
        self.display = display
        self.display.clearDisplay()
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
        time = datetime.now().time()
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # ip = s.getsockname()[0]
        # s.close()

        self.display.display("temp:110",1)
        # self.display.display(ip,3)
        self.display.display(str(time)[:8],4)


