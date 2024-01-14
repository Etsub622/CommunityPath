class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mini=len(blocks)
        count=0
        for i in range(len(blocks)-k+1):
            subs=blocks[i:i+k]
            NoBlack=subs.count("W")
            count=NoBlack
            mini=min(count,mini)
        return mini   


        