class Solution:
    #O(EXPONENTIAL) SC: O(1)
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n= len(s)
        dp= [[-1]*n for _ in range(n)]
        
        def isPalindrome(i, j):
            
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
                
            return True
            
#             if i==j:
#                 dp[i][j]= True
#                 return dp[i][j]
#             if i>j:
#                 dp[i][j]= False
#                 return dp[i][j]
            
#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             if s[i]!= s[j]:
#                 dp[j][j]= False
#                 return False
            
#             ans = isPalindrome(i+1, j-1)
#             dp[i][j]= ans
        
        def recur(idx, path):
            if idx==n:
                # print(idx)
                # print(path)
                ans.append(path)
                return
            
            for i in range(idx, n):
                if isPalindrome(idx, i):
                    newpath= list(path)
                    newpath.append(s[idx:i+1])
                    recur(i+1, newpath)
                    
        recur(0, [])
        return ans
                
            
        
