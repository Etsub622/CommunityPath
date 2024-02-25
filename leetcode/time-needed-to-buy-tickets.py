class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que=deque([i for i in range(len(tickets))])
        output=0
        while que:
            for i in range(len(que)):
                add_end=que.popleft()
                tickets[add_end]-=1
                if tickets[add_end]>0:
                    que.append(add_end)
                output+=1

                if tickets[k]==0:
                    return output
             
       

                
        