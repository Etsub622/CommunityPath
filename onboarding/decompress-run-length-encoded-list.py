class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        i=0
        while i<len(nums):
            n=nums[i]
            output.extend([nums[i+1]]*n)
            i+=2
        return output    

        