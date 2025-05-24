class Solution:
    #TC: O(N) SC: O(1)
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for (i,word) in enumerate(words) if word.find(x) >=0 ]
