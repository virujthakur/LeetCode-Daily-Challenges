class Solution:
    #TC: O(NLOGN) SC:O(N)
    def heightChecker(self, heights: List[int]) -> int:
        expected= sorted(heights)
        count = 0
        for h,v in zip(heights, expected):
            if h!=v:
                count+=1
                
        return count
