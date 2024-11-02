class Solution:
    #TC: O(N) SC: O(1)
    def makeFancyString(self, s: str) -> str:
        s= list(s)
        n = len(s)
        news =[]
        
        i = 0
        while i < n:
            j= i
            cnt = 0
            while j<n and s[j] == s[i]:
                j+=1
                cnt +=1
                
            for k in range(min(cnt, 2)):
                news.append(s[i])
                
            i= j
                
        return ''.join(news)
