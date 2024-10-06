class Solution:
    #TC: O(2*M*N* len(word)) SC: O(2*N*M)
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')
        n = len(words2)
        m = len(words1)
        
        @cache
        def recur1(i, j, isInserted):
            # print(i, j, isInserted)
            if i==m and j==n:
                return True
            
            if i==m and not isInserted:
                return True
            
            if j==n or i==m:
                return False
            
            ans = False
            
            if not isInserted:
                for k in range(j, n):
                    ans |= recur1(i, k+1, True)
                
            if words1[i]== words2[j]:
                ans |= recur1(i+1, j+1, isInserted)
                
               
            return ans
        
        @cache
        def recur2(i, j, isInserted):
            
            if j==n and i==m:
                return True
            
            if j==n and not isInserted:
                return True
            
            if i==m or j==n:
                return False
            
            ans = False
            
            if not isInserted:
                for k in range(i, m):
                    ans |= recur2(k+1, j, True)
                
            if words1[i]== words2[j]:
                ans |= recur2(i+1, j+1, isInserted)
                
               
            return ans
        
        ans1= recur1(0,0, False)
        ans2= recur2(0,0, False)
        # print(ans1, ans2)
        return ans1| ans2
