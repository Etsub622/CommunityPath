class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pProduct=1
        sProduct=1
        output=[0]*len(nums)

        for i in range(len(nums)):
            output[i]=pProduct
            pProduct*=nums[i]
    
        for i in range(len(nums)-1,-1,-1):
            output[i]*=sProduct
            sProduct*=nums[i]
              
        return output           



        