class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        checker=strs[0]
        output=''

        for i in strs:
            if len(i)<len(checker):
                checker=i
                
        for s in range(len(checker)):
            for j in strs:
                if checker[s]==j[s]:
                    pass
                else:
                    return output 
            output+=checker[s] 
                    
        return output                      
        