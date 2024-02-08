class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        store=defaultdict(int)
        n=len(nums)+1
        psum=[0]*n
        for s,e in requests:      
            psum[s]+=1
            psum[e+1]-=1
        
        for i in range(1,n):
            psum[i]+=psum[i-1]
        
        psum.sort(reverse=True)
        print(psum)
        nums.sort(reverse=True)
      
        total=0
        for i in range(len(psum)-1):
            total+=nums[i]*psum[i]
        return total %(10**9 + 7)      
        
        