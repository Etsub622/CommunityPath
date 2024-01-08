class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)     
        output = 0
        for i in nums:
            target = k - i
            if counter[target]>0:
                counter[target]-=1
                output+=1
            else:
                counter[i] +=1
                  
        return (output)  