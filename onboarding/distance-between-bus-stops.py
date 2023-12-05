class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        if start>destination:
            start,destination=destination,start    

        n = len(distance)
        ff= sum(distance[start:destination])
        total = sum(distance)

        return min(ff, total-ff)
        
          

        