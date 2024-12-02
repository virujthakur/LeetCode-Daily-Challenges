class Solution:
    #TC: O(N) SC: O(N)
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i, word in enumerate(sentence):
            prefix = ''
            
            for j in range(len(word)):
                prefix += word[j]
                if prefix == searchWord:
                    return i+1
                
        return -1
