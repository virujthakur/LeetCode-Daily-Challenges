# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #TC: O(N) SC: O(1)
        def dfs(r1, r2):
            
            if r1 == r2 == None:
                return True
            
            if r1 is None or r2 is None:
                return False
            
            if r1.val != r2.val:
                return False
            
            l = dfs(r1.left, r2.right)
            l |= dfs(r1.left, r2.left)
            
            r = dfs(r1.right, r2.right)
            r |= dfs(r1.right, r2.left)
            
            return l & r
        
        return dfs(root1, root2)
