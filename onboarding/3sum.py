class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]

        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue

            l,r=i+1,len(nums)-1
            while l<r:

                s_sum= nums[i]+nums[l]+nums[r]
                if s_sum<0:
                    l+=1
                elif s_sum>0:
                    r-=1
                else:
                    output.append((nums[i],nums[l],nums[r]))  
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1

        return output                 




        