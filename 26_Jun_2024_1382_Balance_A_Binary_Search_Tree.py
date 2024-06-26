# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC: O(N) SC: O(N)
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        v = []
        def inorder(r):
            if r is None:
                return
            
            inorder(r.left)
            v.append(r)
            inorder(r.right)
            
            
        inorder(root)
        v.sort(key= lambda r: r.val)
        n = len(v)
        
        def createBST(i, j):
            if i> j:
                return None
            
            if i==j:
                v[i].left= None
                v[i].right= None
                return v[i]
            
            mid = (i+j)//2
            l = createBST(i, mid-1)
            r = createBST(mid+1, j)
            
            v[mid].left = l
            v[mid].right= r
            return v[mid]
        
        return createBST(0, n-1)
            
            
