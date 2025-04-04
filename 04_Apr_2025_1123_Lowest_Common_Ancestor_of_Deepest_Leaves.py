from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N^2) SC: O(N)
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_map = defaultdict(list)

        def dfs(r, d):
            if r is None:
                return

            depth_map[d].append(r)

            if r.left:
                r.left.parent = r
            if r.right:
                r.right.parent = r

            dfs(r.left, d +1)
            dfs(r.right, d+ 1)


        dfs(root, 0)
        queue = deque()
        visited = set()
        max_depth = max(depth_map)
        num_nodes = len(depth_map[max_depth])

        if num_nodes == 1:
            return depth_map[max_depth][0]

        list_nodes = depth_map[max_depth]

        while True:
            if list_nodes.count(list_nodes[0])== len(list_nodes):
                return list_nodes[0]

            for i in range(num_nodes):
                list_nodes[i] = list_nodes[i].parent
            
        return root

