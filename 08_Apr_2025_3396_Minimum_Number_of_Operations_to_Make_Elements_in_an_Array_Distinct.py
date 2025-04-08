class Solution:
    # TC:O(N) SC: O(N)
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        f= defaultdict(int)
        for num in nums:
            f[num]+=1

        if len(f) == n:
            return 0

        for i in range(n):
            f[nums[i]]-=1
            if f[nums[i]] == 0:
                del f[nums[i]]

            if (i+1)% 3 == 0:
                # print(f, n-i)
                if len(f) == n-i-1:
                    return (i+1)//3

        return int(ceil(n/3))
