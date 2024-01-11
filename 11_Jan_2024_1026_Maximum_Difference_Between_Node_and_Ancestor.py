# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N^2) SC: O(1)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans= 0
        def dfs(r, par):
            nonlocal ans
            if r is None:
                return
            
            ans= max(ans, abs(r.val- par.val))
            dfs(r.left, par)
            dfs(r.right, par)
        
        finalans= 0
        def solve(r):
            nonlocal finalans
            if r is None:
                return
            
            dfs(r, r)
            finalans= max(ans,finalans)
            solve(r.left)
            solve(r.right)
            
        solve(root)
            
        return finalans
            
