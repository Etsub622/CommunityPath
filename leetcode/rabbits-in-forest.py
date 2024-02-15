class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(int)     
        for i in answers:
            dic[i]+=1
        print(dic)    
        ans=0
        final=list(set(answers))
        print(final)
        for i in range(len(final)):
            n=(final[i]+1)*(math.ceil(dic[final[i]]/(final[i]+1)))  

            ans+=int(n)
        return ans      
