class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #TC : O(NK) SC: O(1)
        s = list(s)
        for i,c in enumerate(s):
            s[i]= str(ord(c)- ord('a') + 1)
            
        # print(s)
        for i in range(k):
            su = 0
            for _s in s:
                for c in _s:
                    su += int(c)
              
            news = str(su)
            news = list(news)
            s = news
            
        return int(''.join(s))
                
            
