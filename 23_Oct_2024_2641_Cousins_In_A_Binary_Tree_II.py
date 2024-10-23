# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(N)
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        levelSum =[]
        
        root.val = 0
        q.append(root)
        
        while q:
            sz = len(q)
            s = 0
            
            for i in range(sz):
                cur = q[i]
                if cur.left:
                    s += cur.left.val
                
                if cur.right:
                    s += cur.right.val
                    
            for i in range(sz):
                cur = q.popleft()
                news = s
                if cur.left:
                    news -= cur.left.val
                    
                if cur.right:
                    news -= cur.right.val
                    
                if cur.left:
                    cur.left.val = news
                    q.append(cur.left)
                
                if cur.right:
                    cur.right.val = news
                    q.append(cur.right)
                    
        return root
