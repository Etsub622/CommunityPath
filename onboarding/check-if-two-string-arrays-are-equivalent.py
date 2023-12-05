class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        C1=''
        C2=''
        for i in word1:
            C1+=i
        for j in word2:
            C2+=j
        return C1==C2        
        