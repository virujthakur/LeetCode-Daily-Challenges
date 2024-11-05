class Solution:
    def minChanges(self, s: str) -> int:
        n= len(s)
        @cache
        def recur(idx):
            if idx==n:
                return 0
            
            ans=0
            temp= s[idx:idx+2]
            if temp == "00" or temp == "11":
                ans+= recur(idx+2)
            else:
                ans+= 1+ recur(idx+2)
                
            return ans
        
        return recur(0)
