import threading
import urllib2

class UploadController():
    currentBbqTemp = 0
    airflowPerc = 0

    def __init__(self, stateController):
        stateController.addStateListener(self)
        threading.Timer(2, self.onTimer).start()

    def onTimer(self):
        contents = urllib2.urlopen("http://www.karenvleugel.nl/smokerupload.php?temp="+str(self.currentBbqTemp)+"&fan="+str(self.airflowPerc)).read()
        threading.Timer(10, self.onTimer).start()

    def stateChanged(self, state):
        self.currentBbqTemp = state.bbqTemp
        self.airflowPerc = state.airflowPerc

