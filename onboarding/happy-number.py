class Solution:
    def isHappy(self, n: int) -> bool:
        StorageSet=set()

        while n!=1:
            sum=0 
            for i in str(n):
                sum+=int(i)**2
            n=sum
            if n in StorageSet:
                return False
            else:
                StorageSet.add(n)        
        return True      

            
           
        
        
        