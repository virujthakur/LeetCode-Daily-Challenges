class Solution:
    # TC: O(M*N *LOG(M*N)) SC: O(1) 
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sum(grid, [])
        s= set()
        for num in nums:
            s.add(num % x)

        if len(s) >=2:
            return -1

        nums.sort()
        n = len(nums)
        ans = nums[n//2]
        ops = 0
        for num in nums:
            ops += abs(num - ans) // x

        return ops
