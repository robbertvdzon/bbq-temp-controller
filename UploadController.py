import threading
import urllib2

class UploadController():
    currentBbqTemp = ""
    airflowPerc = ""
    bbqTempSet = ""

    def __init__(self, stateController):
        stateController.addStateListener(self)
        threading.Timer(15, self.onTimer).start()

    def onTimer(self):
        threading.Timer(10, self.onTimer).start()
        contents = urllib2.urlopen("http://www.karenvleugel.nl/smokerupload.php?temp="+self.currentBbqTemp+"&bbqSet="+self.bbqTempSet+"&fan="+self.airflowPerc).read()

    def stateChanged(self, state):
        self.currentBbqTemp = "{0:.2f}".format(state.bbqTemp)
        self.airflowPerc = str(state.airflowPerc)
        self.bbqTempSet = str(state.bbqTempSet)

