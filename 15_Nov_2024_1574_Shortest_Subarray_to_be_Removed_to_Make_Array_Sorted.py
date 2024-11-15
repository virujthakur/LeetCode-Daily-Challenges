class Solution:
    #TC: O(NLOGN) SC: O(1)
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [False] * n
        suffix = [False] * n
        
        prev = -1
        for i in range(n):
            if arr[i] >= prev:
                prefix[i]= True
            else:
                break
            
            prev = arr[i]
            
        
        prev = 10**9 + 1
        for i in range(n-1, -1, -1):
            if arr[i] <= prev:
                suffix[i]= True
            else:
                break
                
            prev = arr[i]
            
            
        l = 0
        h = n-1
        ans = n-1
        
        def isValid(mid):
            for i in range(mid-1, n):
                # print(mid, i)
                if ((i- mid) == -1 or prefix[i- mid]) and (i== n-1 or suffix[i+1] ) and (i- mid == -1 or i== n-1 or arr[i-mid] <= arr[i+1]):
                    return True
                
            return False
        
        while l<= h:
            mid = (l+h) // 2
            if isValid(mid):
                ans = min(ans, mid)
                h = mid-1
            else:
                l = mid+1
                
        return ans
                
            
