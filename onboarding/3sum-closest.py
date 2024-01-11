class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        output = 0
       
        ouput=0

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s_sum = nums[i] + nums[l] + nums[r]
                temp = abs(s_sum - target)

                if temp < diff:
                    diff = temp
                    output = s_sum

                if s_sum < target:
                    l += 1
                elif s_sum > target:
                    r -= 1
                else:
                    return target    
        return output