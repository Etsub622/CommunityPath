class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
          
        output=[]
        evenSum=0
        for i in nums:
            if i%2==0:
                evenSum+=i

        for val,idx in queries:
            old=nums[idx]
            if old%2==0:
                 evenSum-=old

            nums[idx]+=val
            if nums[idx]%2==0:
                evenSum+=nums[idx]
                
            output.append(evenSum)

        return output   

        
        
