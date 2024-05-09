class Solution:
    #TC: O(NLOGN) SC: O(1)
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        ans = 0
        for i, h in enumerate(happiness):
            if i== k:
                break
            ans+= max(0,h-i)
            
        return ans
