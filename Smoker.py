from Display import *
from Encoder import *
from ScreenController import *
from TemperatureController import *
from StateController import *
import time

display = Display()
encoder = Encoder()
stateController = StateController()
temperatureController = TemperatureController(stateController)
screenController = ScreenController(display, encoder, stateController)

try:
    while True:
        time.sleep(0.5)
        screenController.drawScreen()
except KeyboardInterrupt: # Ctrl-C to terminate the program
    GPIO.cleanup()

