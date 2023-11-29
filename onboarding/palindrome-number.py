class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x=x
        if x==0:
            return True
        store=''
        while x>0:
            i=x%10
            store+=str(i)
            x=x//10   
        return store==str(original_x )     
                