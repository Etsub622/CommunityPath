class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        lx,ly=0,0
        output=[]
        while lx<n and ly<n:
            output.append(x[lx])
            output.append(y[ly])

            lx+=1
            ly+=1
        return output    
        