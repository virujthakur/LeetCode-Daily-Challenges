class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l= 1
        h= 10**5
        ans = 10**5 + 1
        
        def isValid(mid):
            st = 0
            for q in quantities:
                st += int(math.ceil(q / mid))
               
            # print(st, mid)
            return st <= n
        
        while l<=h:
            mid = (l+h) // 2
            
            if isValid(mid):
                ans= min(ans, mid)
                h = mid - 1
            else:
                l = mid + 1
                
        return ans
