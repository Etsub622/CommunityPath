# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def symmetric(leftM,rightM):
            if not leftM and not rightM:
                return True
            if not leftM or not rightM:
                return False   
                

            if leftM.val!=rightM.val:
                return False
        
            return symmetric(leftM.left,rightM.right) and symmetric(leftM.right,rightM.left)

        return symmetric(root.left,root.right)    


     


        