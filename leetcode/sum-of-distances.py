class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left=defaultdict(int)
        left_freq=defaultdict(int)
        ans=[0]*len(nums)
        right=defaultdict(int)
        right_freq=defaultdict(int)

        for i in range(len(nums)):
            ans[i]+=left_freq[nums[i]]*i
            ans[i]-=left[nums[i]]

            left_freq[nums[i]]+=1
            left[nums[i]]+=i

        for i in range(len(nums)-1,-1,-1):
            ans[i]-=right_freq[nums[i]]*i
            ans[i]+=right[nums[i]]

            right_freq[nums[i]]+=1
            right[nums[i]]+=i   

        return ans    



                    
        