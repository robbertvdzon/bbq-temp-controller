from Display import *
from Encoder import *
from ScreenController import *
import time

display = Display()
encoder = Encoder()
screenController = ScreenController(display, encoder)

try:
    while True:
        time.sleep(0.5)
        screenController.drawScreen()
except KeyboardInterrupt: # Ctrl-C to terminate the program
    GPIO.cleanup()

