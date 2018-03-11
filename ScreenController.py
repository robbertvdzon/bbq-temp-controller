from datetime import datetime
import socket

class ScreenController:
    display = {}

    def __init__(self, display):
        self.display = display
        self.display.clearDisplay()

    def drawScreen(self):
        time = datetime.now().time()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()

        self.display.display("temp:110",1)
        self.display.display(ip,3)
        self.display.display(str(time)[:8],4)


