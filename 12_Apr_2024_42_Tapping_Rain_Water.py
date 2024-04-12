class Solution:
    #TC: O(N) SC: O(N)
    def trap(self, height: List[int]) -> int:
        n= len(height)
        mxLeft, mxRight = [0]*n, [0]*n
        
        r = 0
        for i in range(n):
            r= max(r, height[n-1-i])
            mxRight[n-1-i] = r
            # print(r)
        
        l = 0
        for i in range(n):
            l= max(l, height[i])
            mxLeft[i] = l
            
        # print(mxRight)
        # print(mxLeft)
            
        ans= 0
        
        for i in range(n):
            ans+= max(0, min(mxLeft[i], mxRight[i])- height[i])
            # print(mxLeft[i], mxRight[i], ans)
        
        return ans
