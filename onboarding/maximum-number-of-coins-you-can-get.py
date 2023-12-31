class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        howMany = n // 3

        output = 0
        j = 2
        for i in range(howMany):
            output += piles[n - j]
            j += 2

        return output
