class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,res,count=0,0,{}
        for i in range(len(answerKey)):
            count[answerKey[i]]=1+count.get(answerKey[i],0)
                
            while i-l+1-max(count.values()) >k:
                count[answerKey[l]]-=1
                l+=1
            res=max(res,i-l+1)               
        return res

    
    
        

               
                


        