class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        psum=[0]*(len(customers)+1)
        acc=0
        for i in range(len(customers)):
            if customers[i]=='Y':
                acc+=1
            psum[i+1]=acc
        final=0   
        ans=psum[-1]
        for i in range(1,len(psum)):
            score = (i -psum[i]) + (psum[-1] - psum[i])
            if ans>score:
                ans=score
                final=i
            
        return final 









          
   





    