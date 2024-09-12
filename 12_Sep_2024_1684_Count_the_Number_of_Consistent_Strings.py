class Solution:
    #TC: O(N* 10) SC: O(1)
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            flag= True
            for c in word:
                if c not in allowed:
                    flag= False
                    break
                    
            if flag:
                ans+=1
                
        return ans
