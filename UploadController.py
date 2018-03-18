import threading
import urllib2

class UploadController():
    currentBbqTemp = 0
    airflowPerc = 0
    bbqTempSet = 0

    def __init__(self, stateController):
        stateController.addStateListener(self)
        threading.Timer(15, self.onTimer).start()

    def onTimer(self):
        threading.Timer(10, self.onTimer).start()
        contents = urllib2.urlopen("http://www.karenvleugel.nl/smokerupload.php?temp="+str(self.currentBbqTemp)+"&bbqSet="+str(self.bbqTempSet)+"&fan="+str(self.airflowPerc)).read()

    def stateChanged(self, state):
        self.currentBbqTemp = state.bbqTemp
        self.airflowPerc = state.airflowPerc
        self.bbqTempSet = state.bbqTempSet

