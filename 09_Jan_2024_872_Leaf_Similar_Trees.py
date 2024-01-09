# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(N)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(r,l):
            if r is None:
                return
            
            if r.left is None and r.right is None:
                l.append(r.val)
            getLeaves(r.left,l)
            getLeaves(r.right,l)
        
        l1=[]
        l2=[]
        getLeaves(root1, l1)
        getLeaves(root2, l2)
        
        return l1 == l2
