class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=path.split('/')
        stack=[]
        for i in paths:
            if i=='..':
                if stack:
                   stack.pop()
                else:
                    pass   
          
            elif i==''or i=='.':
                pass
            else:
                stack.append(i)
        return '/'+ '/'.join(stack)               
        