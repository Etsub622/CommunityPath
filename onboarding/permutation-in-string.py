class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1Count,s2Count={},{}

        for i in range(len(s1)):
            s1Count[s1[i]]=1 +s1Count.get(s1[i],0)
            s2Count[s2[i]]=1 +s2Count.get(s2[i],0)

        if s1Count==s2Count:
            return True
        for r in range(1,len(s2)):
            current=s2[r:r+len(s1)]
            if Counter(current)==s1Count:
                return True
        return False               
                 

        