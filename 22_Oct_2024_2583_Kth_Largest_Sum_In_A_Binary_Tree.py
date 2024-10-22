# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(NLOGN) SC: O(N)
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        levelSum =[]
        
        q.append(root)
        
        while q:
            sz = len(q)
            s = 0
            for i in range(sz):
                cur = q.popleft()
                s += cur.val
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
                    
            levelSum.append(s)
                    
        levelSum.sort(reverse= True)
        return levelSum[k-1] if len(levelSum) >=k else -1
