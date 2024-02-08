class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum=[0]*len(nums)
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            psum[i]=acc
        
        l,output=0,0 
        dic=defaultdict(int)  
        
        for i in range(len(nums)):
            if psum[i]==k:
                output+=1 
            
            target=psum[i]-k
            if target in dic:
                    idx=dic[target]
                    output+=idx    
            dic[psum[i]]+=1   
             
            # while l<i and psum[i]!=k:
            #     psum[i]-=psum[l]
            #     if psum[i]==k:
            #         output+=1       
            #     l+=1
            # l=0    
        return output  
           
                   
     
               