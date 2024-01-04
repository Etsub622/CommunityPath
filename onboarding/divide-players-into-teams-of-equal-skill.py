class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        compare=skill[0]+skill[-1]
        output=skill[0]*skill[-1]

        l,r=1,len(skill)-2
        while l<r:
            if skill[l]+skill[r]!=compare:
                return -1
            output+=skill[l]*skill[r]
            l,r=l+1,r-1
        return output    

                    