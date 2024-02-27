# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans= 0
        def recur(r):
            nonlocal ans
            if not r:
                return 0
            l= recur(r.left)
            r= recur(r.right)
            ans= max(ans,1+l+r)
            
            return 1+max(l,r)
        recur(root)
        return ans-1
