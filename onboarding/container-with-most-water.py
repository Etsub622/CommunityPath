class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r=0,len(height)-1
        volume=0
        while l<=r:
            volume=max(volume,min(height[r],height[l])*(r-l))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return volume        

