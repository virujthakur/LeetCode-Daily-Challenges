# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        v= []
        def inorder(r):
            if r is None: 
                return
            inorder(r.left)
            v.append(r.val)
            inorder(r.right)
            
        i=0
        def inorder2(r):
            nonlocal i
            if r is None:
                return
            
            inorder2(r.left)
            r.val= v[i]
            i+=1
            inorder2(r.right)
            
        inorder(root)
        s= 0
        for i in range(len(v)-1, -1, -1):
            s+= v[i]
            v[i]= s
            
        inorder2(root)
        
        return root
            
