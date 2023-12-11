class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ar=Counter(arr)
        return ar.most_common(1)[0][0]
        