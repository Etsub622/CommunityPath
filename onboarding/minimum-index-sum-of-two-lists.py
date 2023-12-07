class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output=[]
        mini=float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                idx=list2.index(list1[i])
                min_index=i+idx

                if min_index< mini:
                  output=[list1[i]]
                  mini=min_index 

                elif min_index== mini:
                  output.append(list1[i])
        
        return output

    
               

        