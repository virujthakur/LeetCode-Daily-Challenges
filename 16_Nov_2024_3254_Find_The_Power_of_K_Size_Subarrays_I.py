class Solution:
    #TC: O(N*2) SC: O(1)
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            flag= True
            for j in range(i, n):
                
                if i!=j and nums[j]!= nums[j-1] + 1:
                    # print(i, j)
                    flag = False
                    
                if j-i+1 == k:
                    ans.append(nums[j]) if flag else ans.append(-1)
                    
        return ans
                    
                    
