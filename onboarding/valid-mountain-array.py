class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        if arr[0]>=arr[1]:
            return False

        pt=0    
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            if arr[i]>arr[i+1]:
                pt=i
                break
        if pt == 0:
            return False
                 
        for j in range(pt,len(arr)-1):
            if arr[j]<=arr[j+1]:
                return False
        return True        
                  
                      

        


       