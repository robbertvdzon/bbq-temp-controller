import threading, copy, socket

class NetworkController:
    stateController = {}

    def __init__(self, stateController):
        self.stateController = stateController
        threading.Timer(1, self.onTimer).start()

    def onTimer(self):
        try:
            print "strat ip"
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            print "ip="+ip
            s.close()
            self._updateState(ip)
        finally:
            threading.Timer(10, self.onTimer).start()


    def _updateState(self, ip):
        # hou deze functie zo snel mogelijk, om te voorkomen dat we stae changes uit andere threads overschrijven
        oldState = self.stateController.getState()
        newState = copy.copy(oldState)
        newState.ipadress = ip
        self.stateController.updateState(newState)


