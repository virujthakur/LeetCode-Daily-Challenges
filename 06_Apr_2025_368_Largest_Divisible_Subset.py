class Solution:
    #TC: O(N^2) SC: O(N)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans_seq = []
        lis = [1] * n
        par = [-1] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0:
                    if lis[i]+1 > lis[j]:
                        lis[j] = lis[i] + 1
                        par[j] = i

        idx= lis.index(max(lis))
        # print(lis)
        # print(par)

        while idx!= -1:
            ans_seq.append(nums[idx])
            idx= par[idx]

        return ans_seq

        
