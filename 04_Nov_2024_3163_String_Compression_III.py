class Solution:
    #TC: O(N) SC: O(1)
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        ans = ''
        while i<n:
            j = i
            while j< n and j-i+1 <= 9 and word[j] == word[i]:
                j+=1
                
            ans += str(j-i) + word[i]
            
            i = j
            
        return ans
