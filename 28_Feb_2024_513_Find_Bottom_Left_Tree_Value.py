# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res= root.val
        ansLevel= 0
        level= 0
        q= deque()
        q.append(root)
        while q:
            sz= len(q)
            if ansLevel < level:
                res= q[0].val
                
            for i in range(sz):
                x= q[0]
                q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            level+=1
        return res
