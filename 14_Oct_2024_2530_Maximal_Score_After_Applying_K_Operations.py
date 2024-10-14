class Solution:
    #TC: O(NLOGN) SC: O(N)
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        score = 0
        while k:
            x= heapq.heappop(nums)
            score+= -x
            heapq.heappush(nums, -int(ceil(abs(x)/ 3)))
            
            k-=1
            
        return score
            
