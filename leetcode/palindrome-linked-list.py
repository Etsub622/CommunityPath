# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur=slow
        prev=None
        while cur:
            temp=cur.next  
            cur.next=prev
            prev=cur
            cur=temp

        reversedHead=prev
        original=head
        while reversedHead:
            if reversedHead.val!=original.val:
                return False
            original=original.next
            reversedHead=reversedHead.next
        return True        


        
   
