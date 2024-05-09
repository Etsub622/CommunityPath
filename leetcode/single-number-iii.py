class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=0
        ouput=[]
        for i in nums:
            ans^=i
        
        ans=ans & ~(ans-1)
        set1,set2=0,0
        for i in nums:
            if ans & i :
                set1^=i
            else:
                set2^=i
                
        return [set1,set2]                

          
        