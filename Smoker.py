from Display import *
from ScreenController import *
import time

display = Display()
screenController = ScreenController(display)

try:
    while True:
        time.sleep(0.5)
        screenController.drawScreen()
except KeyboardInterrupt: # Ctrl-C to terminate the program
    GPIO.cleanup()

