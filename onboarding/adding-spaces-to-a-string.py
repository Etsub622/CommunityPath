class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output=''
        idx=0

        for i in spaces:
            output+=s[idx:i]
            output+=' '
            idx=i
        output+=s[idx:]    
        return output    

        