# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p and q:
            if p.val != q.val:
                return False
            else:
                ans1= self.isSameTree(p.left,q.left)
                ans2= self.isSameTree(p.right,q.right)
                return ans1 and ans2
        
        return False
