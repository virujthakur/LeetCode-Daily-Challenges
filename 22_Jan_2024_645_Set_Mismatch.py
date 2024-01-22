class Solution:
    #TC: O(N) SC: O(N)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n= len(nums)
        f= defaultdict(int)
        for i in range(n):
            f[nums[i]]+=1
        
        two, missing = -1,-1
        for i in range(n):
            if f[i+1]==2:
                two= i+1
            if f[i+1]==0:
                missing=i+1
                
        return [two, missing]
            
            
