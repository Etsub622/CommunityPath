class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        l,r=0,len(numbers)-1

        while l<r:
            s=numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s< target:
                l+=1
            else:
                output.append(l+1)
                output.append(r+1)
                return output
                
        return output        


        