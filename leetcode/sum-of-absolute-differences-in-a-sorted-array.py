class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pSum=[0]*len(nums)
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            pSum[i]=acc
      
        sSum,pcc=[0]*len(nums),0
        for i in range(len(nums)-1,-1,-1):
            pcc+=nums[i]
            sSum[i]=pcc

            
        ans=[0]*len(nums)
        for i in range(len(nums)):
            left=i*nums[i]-pSum[i]
            right=sSum[i]-(len(nums)-1-i)*nums[i]
            ans[i]=left+right
        return ans          

            
         
        


            
        