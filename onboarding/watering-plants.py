class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        original=capacity
        for i in range(len(plants)):
            if capacity>=plants[i]:
                step+=1
                capacity-=plants[i]
            else:
                
                step+=(i*2)+1
                capacity=original-plants[i]
            print(capacity,step,plants[i])
            
        return step        

        