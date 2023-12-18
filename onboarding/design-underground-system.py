class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.travelTime=defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,startTime=self.checkin[id]
        self.travelTime[(startStation,stationName)].append(t-startTime)
        del self.checkin[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTimes=self.travelTime[(startStation,endStation)]
        return sum(totalTimes)/len(totalTimes)




























# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)