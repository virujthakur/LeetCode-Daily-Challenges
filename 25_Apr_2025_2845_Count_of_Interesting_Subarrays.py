class Solution:
    #TC: O(N) SC: O(N)
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        nums = [1 if num % modulo == k else 0 for num in nums]
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # print(prefix)
        ans = 0
        f = defaultdict(int)

        for i in range(0,n+1):
            ans += f[(prefix[i] + modulo - k) % modulo]
            f[prefix[i] % modulo]+=1

        # print(f)

        return ans
