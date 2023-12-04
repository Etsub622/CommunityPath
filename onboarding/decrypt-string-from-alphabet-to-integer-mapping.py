class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack=[]
        output=''
        for i in s:
            if i!='#':
                stack.append(i)
            else:
                a=stack.pop()
                b=stack.pop()
                output+=b
                output+=a
                stack.append(chr(int(output) + ord('a') - 1))
                output=''
        final=''        
        for j in stack:
            if j.isdigit():
                final+=(chr(int(j) + ord('a') - 1))
            else:
                final+=j
        return final            


              

        