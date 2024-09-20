class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #TC: O(N) SC:O(N)
        def getLongestPalindromicSubstring(s):
            n= len(s)
            rev_s = s[::-1]
            
            p= 37
            mod = 10**9 + 7
            power = [1]* (n+1)
            
            for i in range(1, n+1):
                power[i] = (power[i-1]* p) % mod
                
            rh_prefix = [0]* (n+1)
            for i in range(n):
                rh_prefix[i+1]= (rh_prefix[i]* p + (ord(s[i])- ord('a')+1)) % mod 
                
            rh_suffix = [0]* (n+1)
            
            for i in range(n):
                rh_suffix[i+1]= (rh_suffix[i]+ (ord(s[i])- ord('a')+1) * power[i]) % mod 
            for i in range(n,-1, -1):
                if rh_prefix[i]== rh_suffix[i]:
                    return i
                
            return 0
        
        n= len(s)
        ans_len = getLongestPalindromicSubstring(s)
        return s[ans_len:][::-1] + s
            
            
