class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        valid=0
        nums.sort()
        for i in range(len(nums)-2):
            k=i+2
            if nums[i]==0:
                continue
            if nums[i+1]==0 and nums[-1]==0:
                break    
                
            for j in range(i+1,len(nums)-1):
                while k<len(nums) and nums[i]+ nums[j] > nums[k]:
                    k+=1
                valid+=k-j-1
                   
        return valid        
       


        