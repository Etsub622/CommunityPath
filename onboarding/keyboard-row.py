class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiop"
        second="asdfghjkl"
        third="zxcvbnm"
        output=[]
        for word in words:
            temp=[]
            for i in range(len(word)):
                w=word[i].lower()
                if w in first:
                    temp.append(1)
                elif w in second:
                    temp.append(2)
                else:
                    temp.append(3)
                   
            if len(set(temp))==1:
                output.append(word)
        return output                        

        
            
            
       