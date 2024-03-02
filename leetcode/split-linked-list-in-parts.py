# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
    
        cur = head
        ans= []
        for i in range(k):
            ans.append(None)

        if length <= k:
            i = 0
            while cur:
                ans[i] = ListNode(cur.val)
                cur = cur.next
                i += 1
            return ans   
        else:
            target = length // k
            lst = [target] * k
            left = length % k
            i = 0
            while left > 0:
                lst[i] += 1
                i += 1
                left -= 1

            i = 0
            cur = head
            while i < k and cur:
                ans[i] = ListNode(cur.val)
                prev = ans[i]
                count = 1
                while count < lst[i]:
                    cur = cur.next
                    new_node = ListNode(cur.val)
                    prev.next = new_node
                    prev = new_node
                    count += 1
                cur = cur.next
                i += 1

            return ans    


               
                   
           




        
        