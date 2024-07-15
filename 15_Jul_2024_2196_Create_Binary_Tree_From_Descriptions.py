# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(N)
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root= None
        nodes = {}
        isChild = set()
        for parent, child, isLeft in descriptions:
            
            node = None
            c= None
            
            if parent in nodes:
                node = nodes[parent]
            else:
                node = TreeNode(parent)
                nodes[parent]= node
                
            if child in nodes:
                c = nodes[child]
            else:
                c = TreeNode(child)
                nodes[child]= c
                
            isChild.add(child)
                    
            if isLeft == 1:
                node.left= c
            else:
                node.right= c
        
        for k,v in nodes.items():
            if k not in isChild:
                root= v
                break
                
        return root
