class Solution:
    #TC: O(N) SC: O(1)
    def longestPalindrome(self, s: str) -> int:
        f= defaultdict(int)
        for c in s:
            f[c]+=1
        
        ans = 0
        isPresentOdd = False
        for k,v in f.items():
            if v%2:
                ans+= (v-1)
                isPresentOdd = True
            else:
                ans+= v
                
        return ans + 1 if isPresentOdd else ans
        
