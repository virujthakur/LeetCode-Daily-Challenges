from collections import defaultdict
class Solution:
    #TC: O(N*M) SC: O(1)
    def makeEqual(self, words: List[str]) -> bool:
        freq= defaultdict(int)
        n= len(words)
        for word in words:
            for c in word:
                freq[c]+=1
                
        for k in freq.keys():
            if freq[k]%n > 0:
                return False
        
        return True
