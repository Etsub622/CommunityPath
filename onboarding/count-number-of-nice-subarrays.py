class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pSum=[0]
        curr=0
        for i in nums:
            curr+=i%2
            pSum.append(curr) 

        niceChecker,output={},0
        for i in range(len(pSum)):
            nice=pSum[i]-k
            if nice in niceChecker:
                output+=niceChecker[nice]
            niceChecker[pSum[i]]=1 + niceChecker.get(pSum[i],0)

        return output        



        