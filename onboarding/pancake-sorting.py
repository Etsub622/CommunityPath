class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        count = []
        for i in range(len(arr), 0, -1):
            idx = arr.index(i)
            if idx != i - 1:
                arr[:idx+1] = arr[:idx+1][::-1]
                count.append(idx + 1)
                arr[:i] = arr[:i][::-1]
                count.append(i)
        
        return count
  

        
        