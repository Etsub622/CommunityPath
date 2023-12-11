class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output=[]
    
        location={}
        for i in range(len(boxes)):
            if boxes[i]=='1':
                location[i]=boxes[i]
        for j in range(len(boxes)):
            diff=0
            for k in location.keys():
                diff+=abs(k-j)
            output.append(diff)
        return output        

        