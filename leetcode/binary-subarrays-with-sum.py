class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum=[0]*len(nums)
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            psum[i]=acc
        print(psum) 
        dic=defaultdict(int)   
    
        output=0    
        for i in range(len(nums)):
            if psum[i]==goal:
                output+=1 
            
            target=psum[i]-goal
            if target in dic:
                idx=dic[target]
                output+=idx    
            dic[psum[i]]+=1   
        return output            
                


              

