class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        def columSum(idx):
            colSum=0
            for j in mat:
                colSum+=j[idx]
            return colSum   


        special=0
        for i in mat:
            if sum(i)==1:
                idx=i.index(1)
                if columSum(idx)==1:
                    special+=1
        return special            


            

                
        
                            
 
        