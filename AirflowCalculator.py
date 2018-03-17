
class RegelingRecord:
    verschilMin = 0
    verschilMax = 0
    flow1 = 0
    flow2 = 0
    flow3 = 0
    flow4 = 0
    flow5 = 0

    def __init__(self, verschilMin, verschilMax, flow1, flow2, flow3, flow4, flow5):
        self.verschilMin = verschilMin
        self.verschilMax = verschilMax
        self.flow1 = flow1
        self.flow2 = flow2
        self.flow3 = flow3
        self.flow4 = flow4
        self.flow5 = flow5



class AirflowCalculator():
    DEMPING = 1.0

    KOUDER5 = -100
    KOUDER4 = -50
    KOUDER3 = -20
    KOUDER2 = -10
    KOUDER1 = -5
    ZELFDE = 0
    WARMER1 = 5
    WARMER2 = 10
    WARMER3 = 20
    WARMER4 = 50
    WARMER5 = 100


    regelingen = [
        RegelingRecord(-999,-20, WARMER5,WARMER5,WARMER5,WARMER5,ZELFDE),
        RegelingRecord(-20,-10,  WARMER5,WARMER3,WARMER2,ZELFDE,KOUDER2),
        RegelingRecord(-10,-5,   WARMER4,WARMER2,WARMER1,ZELFDE,KOUDER3),
        RegelingRecord(-5,5,     WARMER3,WARMER1,ZELFDE,KOUDER1,KOUDER3),
        RegelingRecord(5,10,     WARMER2,ZELFDE,KOUDER1,KOUDER2,KOUDER4),
        RegelingRecord(10,20,    ZELFDE,KOUDER1,KOUDER2,KOUDER3,KOUDER4),
        RegelingRecord(20,999,   ZELFDE,KOUDER2,KOUDER3,KOUDER4,KOUDER5)
    ]

    def __init__(self):
        pass

    def calcAirflow(self, bbqTempSet, currentTemp, lastTemp, currentAirflow):
        tempVerschil = currentTemp - bbqTempSet
        tempStijging = currentTemp - lastTemp
        regelingRecord = self.findRecord(tempVerschil)
        if tempStijging<-5:
            return self.calcFlow(currentAirflow,regelingRecord.flow1)
        if tempStijging>=-5 and tempStijging<-1:
            return self.calcFlow(currentAirflow,regelingRecord.flow2)
        if tempStijging>=-1 and tempStijging<1:
            return self.calcFlow(currentAirflow,regelingRecord.flow3)
        if tempStijging>=1 and tempStijging<5:
            return self.calcFlow(currentAirflow,regelingRecord.flow4)
        if tempStijging>=5:
            return self.calcFlow(currentAirflow,regelingRecord.flow5)

    def calcFlow(self, currentAirflow, addedFlow):
        newFlow = int(currentAirflow+addedFlow*self.DEMPING)
        if (newFlow>100):
            newFlow = 100
        if (newFlow<0):
            newFlow = 0
        return int(newFlow)


    def findRecord(self, tempVerschil):
        for record in self.regelingen:
            if (tempVerschil>=record.verschilMin and tempVerschil<=record.verschilMax):
                return record
        return RegelingRecord(111111,111111,self.ZELFDE,self.ZELFDE,self.ZELFDE,self.ZELFDE,self.ZELFDE)
