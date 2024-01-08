# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s= 0
        def preorder(r):
            nonlocal s
            if r is None:
                return
            if r.val >= low and r.val <= high:
                s += r.val
            preorder(r.left)
            preorder(r.right)
        
        preorder(root)
        return s
