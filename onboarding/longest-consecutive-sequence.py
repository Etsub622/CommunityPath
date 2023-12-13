class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        result = 0

        for num in numSet:
            if num - 1 not in numSet: 
                current= num
                length = 1

                while current + 1 in numSet:  
                    current += 1
                    length+= 1

                result = max(result, length) 

        return result

        




        