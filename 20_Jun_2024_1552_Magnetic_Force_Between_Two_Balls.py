class Solution:
    #TC: O(NLOGN) SC: O(1)
    def maxDistance(self, position: List[int], m: int) -> int:
        n= len(position)
        position.sort()
        
        def isValid(mid):
            mf= 10**9
            count = 1
            i=0 
            while i<n:
                r= bisect.bisect_left(position, position[i]+ mid, 0, len(position))
                if r>= n:
                    break
                 
                # print(i,r, mid)
                count+=1
                mf= min(mf, position[r]- position[i])
                i= r
            return count >= m
                
            
        
        l=1
        h= 10**9
        ans = 0
        # print(isValid(3))
        
        while l<=h:
            mid = l+ (h-l)//2
            if isValid(mid):
                ans= max(ans, mid)
                l= mid+1
            else:
                h= mid-1
                
        return ans
