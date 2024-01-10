# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(r):
            nonlocal graph
            if r is None:
                return
            if r.left:
                graph[r.val].append(r.left.val)
                graph[r.left.val].append(r.val)
            if r .right:
                graph[r.val].append(r.right.val)
                graph[r.right.val].append(r.val)
            dfs(r.left)
            dfs(r.right)
        
        dfs(root)
        
        q= deque()
        q.append(start)
        vis= set()
        
        level = 0
        while q:
            sz= len(q)
            for i in range(sz):
                x= q[0]
                vis.add(x)
                q.popleft()
                for y in graph[x]:
                    if y not in vis:
                        q.append(y)
            level+= 1
        
        return level-1
