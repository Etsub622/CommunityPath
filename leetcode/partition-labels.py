class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i,c in enumerate(s):
            last_index[c]=i

        l,r=0,0
        output=[]
        for i,c in enumerate(s):
             
             if last_index[c]>r:
                 r=last_index[c]
             if i==r:
                output.append(r-l+1)
                l=i+1

        return output             


        