class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output=[]
        for i in nums:
            if i<pivot:
                output.append(i)
        for i in nums:
            if i==pivot:
                output.append(i)
        for i in nums:
            if i>pivot:
                output.append(i)    
        return output            
                



        