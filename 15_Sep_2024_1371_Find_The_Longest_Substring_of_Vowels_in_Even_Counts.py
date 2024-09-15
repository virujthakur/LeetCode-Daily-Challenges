class Solution:
    #TC: O(N) SC: O(1)
    def findTheLongestSubstring(self, s: str) -> int:
        n= len(s)
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        
        f= [-1]* 32
        ans = 0
        for i in range(n):
            prefixXOR ^= characterMap[ord(s[i])- ord('a')]
            if f[prefixXOR] == -1 and prefixXOR != 0:
                f[prefixXOR] = i
                
            ans= max(ans, i- f[prefixXOR])
            
        return ans
        
                
        
            
        
        
