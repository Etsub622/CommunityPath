class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack,count=[],0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                    count+=2
        return len(s)-count             

        