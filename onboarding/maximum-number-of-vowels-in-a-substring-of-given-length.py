class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a', 'e', 'i', 'o', 'u']

        l,output=0,0
        hash={}
        for i in range(k):
            if s[i] in vowels:
                hash[s[i]]= 1 + hash.get(s[i],0)
        output = max(output, sum(hash.values()))        
        for r in range(k,len(s)):
            if s[r] in vowels:
                hash[s[r]]= 1 + hash.get(s[r],0)
            if s[l] in  vowels:
                hash[s[l]]-=1
            l+=1    

            output = max(output, sum(hash.values()))

        return output    



        