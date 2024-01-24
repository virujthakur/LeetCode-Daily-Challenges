#TC : O(N) SC: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans= 0
        def dfs(r,cnt):
            nonlocal ans
            if not r:
                return
            
            cnt= list(cnt)
            cnt[r.val]+= 1
            if not r.left and not r.right:
                cntOdd= 0
                for i in range(1,10):
                    if cnt[i]%2:
                        cntOdd+=1
                #print(cntOdd, cntEven)
                #print(cnt)
                if cntOdd<=1:
                    ans+=1
                return
        
            dfs(r.left,cnt)
            dfs(r.right,cnt)
        
        dfs(root, [0]*10)
        return ans
