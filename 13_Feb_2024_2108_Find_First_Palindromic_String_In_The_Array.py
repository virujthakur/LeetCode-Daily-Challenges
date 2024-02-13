class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #TC: O(N*N) SC: O(1)
        def valid(w):
            i,j= 0,len(w)-1
            while i<j:
                if w[i]!= w[j]:
                    return False
                i+=1
                j-=1
            return True
        
        for w in words:
            if valid(w):
                return w
        
        return ""
