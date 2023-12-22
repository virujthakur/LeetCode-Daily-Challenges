class Solution:
    #TC: O(N) SC: O(1)
    def maxScore(self, s: str) -> int:
        total_zeroes= 0
        for c in s:
            if c=='0' :
                total_zeroes+=1
        
        n= len(s)
        # print(total_zeroes)
        ans= 0
        zeroes_in_left= 0
        for i in range(n-1):
            if s[i]=='0':
                zeroes_in_left+=1
                total_zeroes -=1
            
            ones_in_right = (n-1-i)- total_zeroes
            # print(n-1-i, total_zeroes)
            # print(zeroes_in_left, ones_in_right)
            ans= max(ans, zeroes_in_left+ ones_in_right)
            
        return ans
            
            
        
