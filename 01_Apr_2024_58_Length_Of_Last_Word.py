class Solution:
    #TC: O(N) SC: O(N)
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        words= []
        for c in s:
            if c== ' ' :
                if word:
                    words.append(word)
                    word = ''
            else:
                word+= c
                
        if word:
            words.append(word)
            word= ''
            
        return len(words[-1]) if words else 0
