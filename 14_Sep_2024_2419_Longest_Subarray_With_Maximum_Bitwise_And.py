class Solution:
    #TC: O(NLOGN) SC: O(NLOGN)
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix = [[0]* 32 for _ in range(n)]
        
        for j in range(32):
            s= 0
            for i in range(n):
                if (1<<j) & nums[i]:
                    s+=1
                prefix[i][j]= s
              
        # print(prefix)
        
        def computeAND(st, en):
            s = 0
            for j in range(32):
                if st-1>=0:
                    if prefix[en][j] - prefix[st-1][j] == en-st+1:
                        s+= (1<<j)
                else:
                    if prefix[en][j] == en+1:
                        s+= (1<<j)
                        
            return s
        
        
        ans = 1
        prevAnd = 0
        ansAnd = 0
        i, j = 0,0
        for j in range(n):
            newAnd = computeAND(i,j)
            # print(i,j, newAnd)
            if newAnd >= prevAnd and newAnd >=nums[j]:
                if ansAnd < newAnd:
                    ans = j-i+1
                    ansAnd = newAnd
                elif ansAnd == newAnd:
                    ans= max(ans, j-i+1)
                    ansAnd = newAnd
                    
                if ansAnd < nums[j]:
                    ans = 1
                    ansAnd = nums[j]
                elif ansAnd == nums[j]:
                    ans = max(ans, j-i+1)
                    ansAnd = nums[j]
                    
                prevAnd = newAnd
                
                
            else:
                i=j
                prevAnd = nums[i]
                if ansAnd < nums[i]:
                    ansAnd = nums[i]
                    ans = 1
                
        return ans
            
            
            
                    
            
