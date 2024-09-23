class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        #TC: O(N^3) SC: O(N)
        dictionary = set(dictionary)
        n= len(s)
        
        @cache
        def recur(idx):
            if idx== n:
                return 0
            
            substr = ''
            unmatched = 0
            ans = 10**9
            
            for j in range(idx, n):
                substr+= s[j]
                
                if substr in dictionary:
                    ans= min(ans, recur(j+1))
                else:
                    unmatched+=1
                    ans= min(ans, unmatched+ recur(j+1))
                    
            return ans
        
        return recur(0)
