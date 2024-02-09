class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pSum,cur=[],0
        for i in nums:
            cur+=i
            pSum.append(cur)

        divChecker,count={0:1},0
        for i in range(len(pSum)):
            Q=pSum[i]%k
            if Q in divChecker:
                count+=divChecker[Q]

            divChecker[Q]=1+divChecker.get(Q,0)
        return count        


        