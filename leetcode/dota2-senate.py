class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d=deque()
        r=deque()

        n=len(senate)
        for i in range (len(senate)):
            if senate[i]=='D':
                d.append(i)
            else:
                r.append(i)

        while d and r:
            if d.popleft()<r.popleft():
                d.append(n)
            else:
                r.append(n)
            n+=1
        return 'Radiant' if r else 'Dire'            
                        

        