class Solution:
    #TC: O(N) SC: O(1)
    def maxFrequencyElements(self, nums: List[int]) -> int:
        l= Counter(nums).most_common()
        mx= l[0][1]
        ans=0
        for k,v in l:
            if v==mx:
                ans+=v
            else:
                break
        return ans
