class Solution:
    # TC: O(N) SC: O(1)
    def reversePrefix(self, word: str, ch: str) -> str:
        def rev(word, i, j):
            while i<j:
                word[i], word[j] = word[j], word[i]
                i+=1
                j-=1
    
        word = list(word)
        for i,c in enumerate(word):
            if c== ch:
                rev(word, 0, i)
                break
        
        return ''.join(word)
