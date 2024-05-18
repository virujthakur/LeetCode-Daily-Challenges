# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TC: O(N) SC: O(1)
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(r):
            nonlocal ans
            if r is None:
                return 0
            
            left= dfs(r.left)
            right = dfs(r.right)
            
            coins = 0
            if r.val >0 :
                coins = left+ right+ r.val -1
            else:
                coins = left+ right - 1
            
            ans+= abs(coins)
            return coins
        
        dfs(root)
        return ans
        
