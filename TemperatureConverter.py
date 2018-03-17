# import reversed

class TemperatureConverter:
    listOfCalibrationValuesBbq = [
        (1620,0),
        (1580,10),
        (1537,20),
        (1484,30),
        (1416,40),
        (1318,50),
        (1207,60),
        (1075,70),
        (943,80),
        (815,90),
        (673,100),
        (510,110),
        (415,120),
        (335,130),
        (290,140),
        (232,150),
        (195,160),
        (172,170),
        (141,180),
        (113,190),
        (94,200),
        (55,230),
        (30,300)
         ]

    listOfCalibrationValuesMeat = [
        (1620,100),
        (30,300)
    ]

    def convertBbq(self, value):
        return self._convert(value, self.listOfCalibrationValuesBbq)

    def convertMeat(self, value):
        return self._convert(value, self.listOfCalibrationValuesMeat)

    def _convert(self, value, calibrationList):
        lowCalibrationValue = self.getLowCalibration(value, calibrationList)
        highCalibrationValue = self.getHighCalibration(value, calibrationList)

        lowVal = lowCalibrationValue[0]
        highVal = highCalibrationValue[0]
        highTemp = lowCalibrationValue[1]
        lowTemp = highCalibrationValue[1]


        if (value==lowVal) : return lowTemp
        if (value==highVal) : return highTemp

        valueDelta = highVal-lowVal
        tempDelta = highTemp - lowTemp

        tempDiffPerValue = tempDelta/float(valueDelta)
        temp = highTemp - tempDiffPerValue*(value-lowVal)
        return int(temp)

    def getLowCalibration(self, value, calibrationList):
        for cal in calibrationList:
            calValue = cal[0]
            if (calValue<=value): return cal
        return (0,1000)   # when not found

    def getHighCalibration(self, value, calibrationList):
        for cal in reversed(calibrationList):
            calValue = cal[0]
            if (calValue>=value): return cal
        return (99999,-100)   # when not found
