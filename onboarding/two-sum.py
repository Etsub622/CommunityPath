class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output={}
        for i,num in enumerate(nums):
            res=target-nums[i]  
            if res in output:
                return(i,output[res])
            else:
                output[num]=i 
        return output
      
           
                
            
        