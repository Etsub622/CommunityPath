# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que=deque([root])
        ans=[]
        flag='fromR'
        
        while que:
            curr=deque()
            n=len(que)

            for _ in range(n):
                node=que.popleft() 
                if flag=='fromR':  
                    curr.append(node.val)           
                else:
                    curr.appendleft(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                    
            ans.append(list(curr))
            flag='fromL' if flag=='fromR' else 'fromR'
        return ans   

          
        
    


       

    
     
           


        

    
        
