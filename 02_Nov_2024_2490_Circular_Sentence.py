class Solution:
    #TC: O(N) SC: O(1)
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        n = len(sentence)
        for i in range(1,n):
            if sentence[i][0] != sentence[i-1][-1]:
                return False
            
        return sentence[-1][-1] == sentence[0][0]
