import bisect
class Solution:
    #TC: O(NLOGN) SC:O(1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp =[]
        for num in nums:
            idx= bisect.bisect_left(temp,num,0,len(temp))
            if idx == len(temp):
                temp.append(num)
            else:
                temp[idx]= min(temp[idx],num)
        
        return len(temp)
