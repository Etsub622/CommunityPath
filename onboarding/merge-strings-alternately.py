class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=0,0
        output=''
        while l1<len(word1) and l2<len(word2):
            output+=word1[l1]
            output+=word2[l2]
            l1+=1
            l2+=1
        if l1:
            output+=word1[l1:]
        if l2:
            output+=word2[l2:]
        return output



        
        