class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output=0

        for i in range(len(strs[0])):
            column=[]
            for j in strs:    
                column.append(j[i])
            checker=sorted(column)
            if checker!=column:    
               output+=1
        return output  
        