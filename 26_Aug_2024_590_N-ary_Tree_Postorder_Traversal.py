"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#TC : O(N) SC: O(1)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        answer= []
        def postorder(r):
            if r is None:
                return
            
            for n in r.children:
                postorder(n)
                
            answer.append(r.val)
            
        postorder(root)
        return answer
