class Solution:
    #TC: O(N^2LOGN) SC: O(N)
    def canSortArray(self, nums: List[int]) -> bool:
        n= len(nums)
        def cntbits(temp):
            cnt = 0
            while temp > 0:
                if temp%2 ==1:
                    cnt+=1
                temp//=2
            return cnt
        
        i=0
        j=0
        
        while j<n:
            templist= []
            tempidx = []
            while j<n and cntbits(nums[j]) == cntbits(nums[i]):
                templist.append(nums[j])
                tempidx.append(j)
                j+=1
            
            templist.sort()
            for val, tempidx in zip(templist, tempidx):
                nums[tempidx]= val
                
            i=j
                    
        return nums== sorted(nums)
