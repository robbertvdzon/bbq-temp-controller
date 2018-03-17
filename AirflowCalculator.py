
class AirflowCalculator():

    def calcAirflow(self, bbqTempSet, currentTemp, lastTemp):
        print "tempSet="+str(bbqTempSet)+" curr:"+str(currentTemp)+ "  last="+str(lastTemp)
        return bbqTempSet+2
