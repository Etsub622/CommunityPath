# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def frequent(root,store):
            if not root:
                return 

            store[root.val] += 1    
            frequent(root.left,store)
            store[root.val] += 1
            frequent(root.right,store)
        store=defaultdict(int)
        frequent(root,store)

        mode=[]
        maxi=max(store.values())
        for i in store:
            if store[i]==maxi:
                mode.append(i)       
        return mode        
        