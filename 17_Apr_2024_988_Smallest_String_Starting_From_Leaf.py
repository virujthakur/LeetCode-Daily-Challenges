# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC: O(N^2) SC: O(1)
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = ''
        
        def dfs(root, path):
            nonlocal ans
            if root is None:
                return
            
            if root.left is None and root.right is None:
                path = path+ chr(ord('a')+ root.val)
                rev= path[::-1]
                if ans == '':
                    ans= rev
                else:
                    ans = min(ans, rev)
                    
                return
                
            dfs(root.left, path+ chr(ord('a')+ root.val))
            dfs(root.right, path+ chr(ord('a')+ root.val))
    
        dfs(root, '')
        return ans
            
