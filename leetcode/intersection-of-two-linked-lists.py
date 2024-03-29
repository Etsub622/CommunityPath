# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1=headA
        cur2=headB
        dic=defaultdict(int)
        if cur1.next==None and cur2.next==None:
            if cur1.val==cur2.val:
               return cur1
                
        while cur1:
            dic[cur1]=cur1.val
            cur1=cur1.next
        
        while cur2:
            if cur2 in dic:
                return cur2
            cur2=cur2.next    
        return       




        