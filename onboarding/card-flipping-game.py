class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        Uniquecards=set(fronts+backs)

        for i in range(len(fronts)):
            if fronts[i]==backs[i] and fronts[i] in Uniquecards:
                Uniquecards.remove(fronts[i])
        return Uniquecards.pop() if len(Uniquecards)!=0 else 0        

        
     

        