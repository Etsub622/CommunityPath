class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        output = ''
        for i in range(0, len(s), 2*k):
            sFirst = s[i:i+k]
            reverse = sFirst[::-1]
            output += reverse + s[i+k:i+2*k]
        return output
        