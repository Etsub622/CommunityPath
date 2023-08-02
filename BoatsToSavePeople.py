class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        count = 0
        l, r = 0, len(people) - 1
        peoples = sorted(people)
        
        while l <= r:
            if peoples[l] + peoples[r] <= limit:
                l += 1
            r -= 1
            count += 1
  
        return count  
