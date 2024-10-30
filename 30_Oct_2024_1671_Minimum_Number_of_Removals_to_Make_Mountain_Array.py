class Solution:
    #TC: O(N^2) SC: O(N^2)
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]* n
        lds = [1]* n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1+ lis[j])
                    
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    lds[i]= max(lds[i], 1 + lds[j])
                    
        ans = 0
        for i in range(n):
            if lds[i] > 1 and lis[i] > 1:
                ans = max(ans, lds[i]+ lis[i] -1)
            
        return n- ans
