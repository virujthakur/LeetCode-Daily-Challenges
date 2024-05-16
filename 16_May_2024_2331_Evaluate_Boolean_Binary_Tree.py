# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            
            if r.left is None and r.right is None:
                return r.val
            
            left = dfs(r.left)
            right= dfs(r.right)
            
            if r.val == 2:
                return right or left
            else:
                return right and left
            
        return dfs(root)
            
