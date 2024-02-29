# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        level= 0
        q= deque()
        q.append(root)
        while q:
            sz= len(q)
            if level % 2 == 0:
                prev= -1
                for i in range(sz):
                    x= q[0]
                    if x.val % 2 == 0:
                        return False
                        
                    if x.val <= prev:
                        return False
                    q.popleft()
                    if x.left:
                        q.append(x.left)
                    if x.right:
                         q.append(x.right)
                    prev= x.val
            else :
                prev= 10**9
                for i in range(sz):
                    x= q[0]
                    if x.val % 2:
                        return False
                    if x.val >= prev:
                        return False
                    q.popleft()
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
                    prev= x.val
            level+=1
        return True
