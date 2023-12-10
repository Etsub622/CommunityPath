class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive,negative=[],[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)

        p,n=0,0
        output=[]
        while n<len(negative) and p<len(positive):
            output.append(positive[p])
            output.append(negative[n])
            p+=1  
            n+=1
        return output    
