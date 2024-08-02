class Solution:
    #TC: O(N) SC: O(1)
    def minSwaps(self, nums: List[int]) -> int:
        cnt_ones = 0
        for num in nums:
            if num == 1:
                cnt_ones+=1
                
        if cnt_ones == 0 or cnt_ones== len(nums):
            return 0
                
        nums = nums+ nums
        n= len(nums)
        
        ans = 10**9
        cnt_zeroes = 0
        for i in range(cnt_ones-1):
            if nums[i] == 0:
                cnt_zeroes+=1
                
        for j in range(cnt_ones-1, n):
            if nums[j]== 0:
                cnt_zeroes+=1
                
            ans= min(ans, cnt_zeroes)
            
            if nums[j- cnt_ones + 1]==0:
                cnt_zeroes-=1
                
        return ans
        
        
            
