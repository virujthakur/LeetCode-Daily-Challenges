class Solution:
    def numberOfMatches(self, n: int) -> int:
        # TC: O(LOGN) SC: O(1)
        matches = int(0)
        while n > 1 :
            # print(n)
            matches+= int(n/2)
            if (int(n) %2) == 1:
                n= int(n/2) +1
            else:
                n= int(n/2)
        
        return matches
            
            
        
