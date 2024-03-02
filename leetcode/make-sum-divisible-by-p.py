class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        mod_initial= sum(nums)%p  
        
        output=len(nums)
        dic=defaultdict(int)  
        dic[0]=-1
        cur=0

        for i in range(len(nums)): 
            cur+=nums[i]
            target=(cur%p-mod_initial)%p
            if target in dic:
                output=min(i-dic[target],output)   
            dic[cur%p]=i   

        return -1 if output>=len(nums) else output

               

                     
            
        