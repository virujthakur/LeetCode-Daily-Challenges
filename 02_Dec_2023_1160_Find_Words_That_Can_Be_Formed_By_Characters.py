from collections import defaultdict
class Solution:
    # n = len(words) m= len(words[i])
    #TC : O(N * M) SC: O(26)
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = defaultdict(int)
        ans=0
        for c in chars:
            freq[c]+=1
        for word in words:
            temp = freq.copy()
            for ch in word:
                temp[ch]-=1
            
            flag = True
            for key,val in temp.items():
                if val < 0:
                    flag= False
                    break
            if flag:
                ans += len(word)
        
        return ans
