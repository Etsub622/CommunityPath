class Solution:
    def isValid(self, s: str) -> bool:
       
        stack=[]
        valid={"(":")","[":"]","{":"}"}
        opening=["(","[","{"]

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if stack and valid[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return stack==[]



                     
