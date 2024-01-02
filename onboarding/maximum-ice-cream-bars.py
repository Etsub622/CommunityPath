class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        output=0
        final=0
        for i in costs:
            output+=i
            if output<=coins:   
                final+=1
                    
        return final        
                
