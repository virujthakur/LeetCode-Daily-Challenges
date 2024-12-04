class Solution:
    #TC: O(N) SC: O(1)
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        n = len(str2)
        m = len(str1)
        j = 0
        for i in range(n):
            
            c2 = chr(ord(str2[i])-1) if str2[i] != 'a' else 'z'
            
            while j< m and str1[j]!= str2[i] and str1[j] != c2:
                j+=1
             
            # print(i, j)
            if j ==m:
                return False
            
            
            j+=1
                
        return True
            
            
