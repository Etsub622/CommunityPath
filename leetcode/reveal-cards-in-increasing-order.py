class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort(reverse=True)
        ans=deque(deck)
        dq=deque()
    
        for i in range(len(ans)):
            if len(dq)>1:
                
                dq.appendleft(dq.pop())         
            dq.appendleft(ans.popleft())
        return dq        

       
        