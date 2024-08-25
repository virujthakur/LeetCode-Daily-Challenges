# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC : O(N) SC: O(1)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postorder(r):
            if r is None:
                return
            
            postorder(r.left)
            postorder(r.right)
            answer.append(r.val)
            
        postorder(root)
        return answer
            
            
        
        
