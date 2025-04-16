class Solution:
    #TC: O(N) SC: O(1)
    def countGood(self, nums: List[int], k: int) -> int:
        i=0
        n = len(nums)
        ans = 0
        cnt = 0
        f = defaultdict(int)
        for j in range(n):
            cnt += f[nums[j]]
            f[nums[j]] +=1
            
            while i<=j and cnt >=k:
                # print(i, j, cnt)
                # print(n-j, cnt)
                ans += n-j
                f[nums[i]] -=1
                cnt -= f[nums[i]]
                i+=1

        return ans
