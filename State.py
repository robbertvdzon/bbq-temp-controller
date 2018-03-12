
class State:
    bbqTemp=0
    meatTemp=0
    bbqTempSet=0
    meatTempSet=0
    ipadress='unknown'
    valvePercOpen=0
    fanOn=False
    forceCloseAirflow=False

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

