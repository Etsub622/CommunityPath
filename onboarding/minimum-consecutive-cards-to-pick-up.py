class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l=0
        output=len(cards)+1
        freq=defaultdict(int)
        for i in range(len(cards)):
            freq[cards[i]]+=1

            while freq[cards[i]]>1:
                output=min(output,i-l+1)
                freq[cards[l]]-=1
                l+=1

                if freq[cards[i]]==0:
                    del freq[i]
        return output if output!=len(cards)+1 else -1            



        