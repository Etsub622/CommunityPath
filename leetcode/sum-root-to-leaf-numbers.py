# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total=0
        def TotalSum(node,curSum):
            nonlocal total
            if not node:   
                total+=int(curSum)
                return 
            
            if node.left and node.right:
                TotalSum(node.left,curSum+str(node.val))
                TotalSum(node.right,curSum+str(node.val))
            elif node.left:
                TotalSum(node.left,curSum+str(node.val))
            else:
                TotalSum(node.right,curSum+str(node.val)) 
                  


        TotalSum(root,'')
        return total  

        