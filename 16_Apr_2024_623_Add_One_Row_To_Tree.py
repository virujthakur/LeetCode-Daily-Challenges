# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        depth -=1
        if depth == 0:
            newroot = TreeNode(val)
            newroot.left= root
            return newroot
        
        def dfs(root, level):
            nonlocal depth
            nonlocal val
            if root is None:
                return
            
            if level== depth-1:
                l= root.left
                r= root.right
                root.left = TreeNode(val)
                root.right = TreeNode(val)
                
                root.left.left = l
                root.right.right = r
                
            dfs(root.left, level+1)
            dfs(root.right, level+1)
            
        dfs(root, 0)
        return root
