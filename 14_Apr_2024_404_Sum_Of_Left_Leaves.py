# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if root is None:
                return
            if root.left and root.left.left is None and root.left.right is None:
                ans+= root.left.val
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ans
