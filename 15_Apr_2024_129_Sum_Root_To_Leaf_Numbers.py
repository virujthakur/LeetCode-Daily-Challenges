# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        s= 0
        def dfs(root, num):
            nonlocal s
            if root is None:
                return 
            if root.left is None and root.right is None:
                s+= num*10+ root.val
                return
            
            dfs(root.left, num* 10 + root.val)
            dfs(root.right, num* 10 + root.val)
            
        dfs(root, 0)
        return s 
