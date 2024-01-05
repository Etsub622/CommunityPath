class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
            storageSet=set()
            l=0
            output=0
            for i in range(len(s)):
                while s[i] in storageSet:
                    storageSet.remove(s[l])
                    l+=1
                storageSet.add(s[i])
                output=max(output,len(storageSet))
            return output
               



