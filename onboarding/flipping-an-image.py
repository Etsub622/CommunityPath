class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output=[]
        for i in image:
            out=[]
            for j in range(len(i)):              
                if i[j]==0:
                    out.append(1)
                else:
                    out.append(0)  
            out.reverse()
            output.append(out)
        return output          


        