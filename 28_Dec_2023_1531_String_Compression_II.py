class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n= len(s)
        # N * (N+1) * 27 * (N+1)
        dp=  {}
                        
        # print(dp[0][0])
        
        def recur(idx, _k, prevChar, prevCharCnt):
            if _k < 0:
                return 10 ** 9
            if idx == n :
                return 0
            
            key = idx* 101* 27* 101+ _k* 27*101 + (ord(prevChar)- ord('a'))* 101 + prevCharCnt
            if key in dp:
                return dp[key]
            
            ans1= recur(idx+1, _k-1, prevChar, prevCharCnt)
            
            ans2= 0
            if s[idx]== prevChar:
                ans2= recur(idx+1, _k, prevChar, prevCharCnt+1) + (1 if prevCharCnt in [1,9,99] else 0)
            else:
                ans2= 1+ recur(idx+1, _k, s[idx], 1)
            
            dp[key] = min(ans1, ans2)
            return min(ans1, ans2)
        
        # print(chr(123))
        return recur(0, k, '{', 0)
                                                                
                
