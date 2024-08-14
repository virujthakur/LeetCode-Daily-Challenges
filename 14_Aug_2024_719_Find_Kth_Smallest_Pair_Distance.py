class Solution:
    #TC: O(NLOGN *LOGN) SC: O(1)
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = 0
        h = 10**6
        ans = 10**9
        n = len(nums)
        
        def isValid(dist):
            cnt = 0
            
            for i in range(n):
                j= bisect.bisect(nums, nums[i]+ dist, i+1, n)
                cnt += j-i-1
                
            # print(mid, cnt)
            return cnt >= k
                
        
        while l<=h:
            mid = l + (h-l) // 2
            if isValid(mid):
                ans = min(ans, mid)
                h= mid-1
            else:
                l= mid+1
                
        return ans
