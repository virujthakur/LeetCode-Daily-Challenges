class Solution:
    #TC: O(N*27) SC: O(1)
    def longestIdealString(self, s: str, k: int) -> int:
        n= len(s)
        dp= [[-1]* 27 for _ in range(n)]
        def recur(i, prev):
            if i == len(s):
                return 0
            
            if dp[i][abs(ord(prev)- ord('a'))] != -1:
                return dp[i][abs(ord(prev)- ord('a'))]
            
            ans2= 0
            ans1= recur(i+1, prev)
            if prev== "{" or abs(ord(s[i])- ord(prev)) <=k:
                ans2= 1+ recur(i+1, s[i])
             
            dp[i][abs(ord(prev)- ord('a'))] = max(ans1, ans2)
            return max(ans1, ans2)
        
        # print(chr(ord('z')+1))
        return recur(0, chr(ord('z')+1))
        
                
