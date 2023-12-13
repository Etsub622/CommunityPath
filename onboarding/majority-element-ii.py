class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1 or len(nums)==2:
            return set(nums)
        num=Counter(nums)
        
        final=set()
        for i,c in num.items():
            if c>len(nums)//3:
                final.add(i) 
       
        return final    

        