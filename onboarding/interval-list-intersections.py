class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l,r=0,0
   
        output = []
        while l < len(firstList) and r < len(secondList):
            a=max(firstList[l][0],secondList[r][0])
            b=min(firstList[l][1],secondList[r][1])
            if a<=b:
                output.append([a,b])

            if firstList[l][1]<secondList[r][1]:
                l+=1
            else:
                r+=1
        return output            
                


            

        