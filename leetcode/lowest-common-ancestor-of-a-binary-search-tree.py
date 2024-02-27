# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root.left or not root.right:
        #     return p
        # if (lef.val==p or lef.val==q) and (righ.val==p or righ.val==q):
        #     return root 
        # lef=self.lowestCommonAncestor(root.left,p,q)
        # righ=self.lowestCommonAncestor(root.right,p,q)
        p_path,q_path=[],[]
        def common(root,val,path):
            path.append(root)
            if val==root.val:
                return
            if val>root.val:
                common(root.right,val,path)
            else:
                common(root.left,val,path)
        common(root,p.val,p_path)
        common(root,q.val,q_path)

        for i in range(min(len(p_path),len(q_path))):
            if p_path[i]!=q_path[i]:
                return p_path[i-1]
                          

        return p_path[-1] if len(p_path)<len(q_path) else q_path[-1]