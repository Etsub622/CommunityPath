class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        for i in arr2:
            num=arr1.count(i)
            output.extend([i]*num)
        Left=[]    
        for j in arr1:
            if j not in output:
                Left.append(j)
        Left.sort()            
        return (output+Left)    

        