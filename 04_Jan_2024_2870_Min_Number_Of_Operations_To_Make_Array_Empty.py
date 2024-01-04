class Solution:
    #TC: O(N) SC: O(N)
    def minOperations(self, nums: List[int]) -> int:
        n= len(nums)
        freq =  defaultdict(int)
        for num in nums:
            freq[num]+=1
            
        ans=0
        for k in freq.keys():
            if freq[k]== 1:
                return -1
            
            if freq[k]% 3 == 2 or freq[k]%3 == 1:
                ans += freq[k]//3 + 1
            else :
                ans+= freq[k]//3
                
        return ans
                
