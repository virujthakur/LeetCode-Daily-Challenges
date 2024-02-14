class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #TC: O(2N) SC: O(N)
        p,n= [],[]
        for nu in nums:
            if nu>0:
                p.append(nu)
            else:
                n.append(nu)
            
        ans= []
        for a,b in zip(p,n):
            ans.append(a)
            ans.append(b)
        return ans
