class Solution:
    def interpret(self, command: str) -> str:
        stack=[]
        for i in range(len(command)):
            if command[i]!=')':
                stack.append(command[i])
            else:
                if stack[-1]=='(':  
                    stack.pop()
                    stack.append('o')
                else:
                    while stack[-1]!='(':
                        stack.pop()
                    stack.pop()
                    stack.append('a')
                    stack.append('l')
        output=''.join(stack) 
        return output
