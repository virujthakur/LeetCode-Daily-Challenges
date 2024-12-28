class Solution:
    #TC: O(N*4) SC: O(N*4)
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[-1] * 4 for __ in range(n)]
        path = [[-1 for _ in range(4)] for __ in range(n)]

        def recur(idx, cnt):
            if cnt == 0:
                return 0
            if idx >= n or cnt < 0:
                return -10**9
            if dp[idx][cnt] != -1:
                return dp[idx][cnt]
            
            # Take the subarray starting at idx
            if idx + k > n:
                return -10**9
            current_sum = sum(nums[idx:idx + k])
            take = current_sum + recur(idx + k, cnt - 1)
            
            # Don't take the subarray
            not_take = recur(idx + 1, cnt)
            
            if take >= not_take:
                path[idx][cnt] = idx  # Store the start index of the subarray
                dp[idx][cnt] = take
            else:
                path[idx][cnt] = path[idx + 1][cnt]  # Skip to the next index
                dp[idx][cnt] = not_take
            
            return dp[idx][cnt]
        
        # Compute the maximum sum
        s = recur(0, 3)
        # print(s)
        # print(path)

        # Backtrack to find the indices
        res = []
        idx, cnt = 0, 3
        while cnt > 0:
            start_idx = path[idx][cnt]
            res.append(start_idx)
            idx = start_idx + k
            cnt -= 1
        
        return res
