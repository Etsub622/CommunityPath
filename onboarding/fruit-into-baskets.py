class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,dic=0,defaultdict(int)
        output=0

        for i in range(len(fruits)):
            dic[fruits[i]]+=1

            while len(dic)>2:  
                dic[fruits[l]]-=1  
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l+=1
            output=max(output,i-l+1)    
        return output            



        