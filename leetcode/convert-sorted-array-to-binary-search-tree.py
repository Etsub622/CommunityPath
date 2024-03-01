# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l,r):
            if l>r:
                return None
            m=(l+r)//2
            l=bst(l,m-1)
            r=bst(m+1,r)
            return TreeNode(nums[m],l,r)
        return bst(0,len(nums)-1)     
        