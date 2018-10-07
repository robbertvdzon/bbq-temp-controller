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
        data = urllib.urlencode({'bbqtemp' :self.currentBbqTemp,'meattemp'  : self.currentMeatTemp, 'bbqtempset' : self.bbqTempSet, 'fan' : self.airflowPerc})
        contents = urllib2.urlopen("https://mysmoker.api.vdzon.com/add/", data).read()

content = urllib2.urlopen(url=url, data=data).read()

    def stateChanged(self, state):
        self.currentBbqTemp = "{0:.2f}".format(state.bbqTemp)
        self.airflowPerc = str(state.airflowPerc)
        self.bbqTempSet = str(state.bbqTempSet)
        self.currentMeatTemp = "{0:.2f}".format(state.meatTemp)

