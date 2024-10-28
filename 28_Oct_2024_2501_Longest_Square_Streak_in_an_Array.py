class Solution:
    #TC: O(NLOGN) SC: O(N)
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        visited = [False]* n
        res = -1
        for i in range(n):
            if visited[i]== True:
                continue
            
            ans = 1
            cur = i
            j= i+1
            while j < n:
                j= bisect.bisect_left(nums, nums[cur]* nums[cur], cur+1, n)
                
                if j== n or nums[j] != nums[cur]* nums[cur]:
                    break
                
                visited[j] = True
                cur = j
                ans += 1
                res = max(ans, res)
                
        return res if res > 1 else -1
                
            
                
            
                
            
