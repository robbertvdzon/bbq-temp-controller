import threading
import urllib2

class UploadController():
    currentBbqTemp = ""
    currentMeatTemp = ""
    airflowPerc = ""
    bbqTempSet = ""

    def __init__(self, stateController):
        stateController.addStateListener(self)
        threading.Timer(15, self.onTimer).start()

    def onTimer(self):
        threading.Timer(10, self.onTimer).start()
        contents = urllib2.urlopen("https://mysmoker.api.vdzon.com/add/"+self.currentBbqTemp+"/"+self.currentMeatTemp+"/"+self.bbqTempSet+"/"+self.airflowPerc).read()

    def stateChanged(self, state):
        self.currentBbqTemp = "{0:.2f}".format(state.bbqTemp)
        self.airflowPerc = str(state.airflowPerc)
        self.bbqTempSet = str(state.bbqTempSet)
        self.currentMeatTemp = "{0:.2f}".format(state.meatTemp)

