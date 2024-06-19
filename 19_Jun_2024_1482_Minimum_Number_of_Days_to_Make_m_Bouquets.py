class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n= len(bloomDay)
        
        def isValid(mid):
            consec = 0
            ans = 0
            for i in range(n):
                if bloomDay[i]<= mid:
                    consec+=1
                else:
                    ans+= consec//k
                    consec = 0
              
            if consec > 0:
                ans+= consec//k
            # print(ans, mid)
            return ans >=m
        
        l=1
        h=10**9
        ans = 10**9+1
        
        while l<=h:
            mid = l + (h-l)//2
            if isValid(mid):
                ans= min(ans, mid)
                h= mid-1
            else:
                l= mid+1
                
        return ans if ans <= 10**9 else -1
        
            
