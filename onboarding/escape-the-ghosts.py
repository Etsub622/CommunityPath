class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        output=[]
        for ghost in ghosts:
            diff=abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            output.append(diff)
        me=abs(0-target[0]) + abs(0-target[1]) 

        for i in output:
            if i<=me:
                return False
        return True
