class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            nums = list(str(num))
            if '0' in nums:
                zeros = nums.count('0')
                nums = [digit for digit in nums if digit != '0']
                nums.sort()
                nums.insert(1, '0' * zeros)
            else:
                nums.sort()
        else:
            nums = list(str(abs(num)))
            if '0' in nums:
                zeros = nums.count('0')
                nums = [digit for digit in nums if digit != '0']
                nums.sort(reverse=True)
                nums.insert(len(nums), '0' * zeros)
            else:
                nums.sort(reverse=True)

        return int(''.join(nums)) if num > 0 else -int(''.join(nums))
