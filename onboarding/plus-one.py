class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output=''
        for i in digits:
            output+=str(i)
        out=str((int(output))+1)
        output=[]
        for i in out:
            output.append(int(i))
        return output    

           
            
        
      

        
        