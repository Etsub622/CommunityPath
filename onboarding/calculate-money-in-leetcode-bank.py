class Solution:
    def totalMoney(self, n: int) -> int:
        res = n // 7
        remain = n % 7

        if n < 7:
            return (n * (n + 1)) // 2
        else:
            result = (res * 28) + (7 * res * (res - 1) // 2) + (remain * (2 * res + remain + 1) // 2)
            return result