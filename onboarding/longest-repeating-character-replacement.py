class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        S_count={}
        output=0
        for i in range(len(s)):
            S_count[s[i]]=1+ S_count.get(s[i],0)

            while (i-l+1)- max(S_count.values())>k:
                S_count[s[l]]-=1
                l+=1
            output=max(output,i-l+1)
        return output        



       

                    

                

        