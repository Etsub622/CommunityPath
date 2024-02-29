# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,small,high):
            
            if not node:
                return True

            if not small<node.val<high:
                return  False

            validateleft=validate(node.left,small,node.val)
            
            validateright=validate(node.right,node.val,high)
            
            return validateleft and validateright 
              
        return validate(root,-inf,inf)



        