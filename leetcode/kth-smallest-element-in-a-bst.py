# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final=[]
        def Inorder(node):
            nonlocal final
            if not node:
                return []
            Inorder(node.left)
            final.append(node.val)
            Inorder(node.right)

        Inorder(root)
        return final[k-1]

        