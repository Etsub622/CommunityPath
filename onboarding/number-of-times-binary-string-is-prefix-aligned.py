class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        maxi=0
        for i in range(len(flips)):
            maxi=max(maxi,flips[i])
            if maxi==i+1:
                count+=1
        return count        

        