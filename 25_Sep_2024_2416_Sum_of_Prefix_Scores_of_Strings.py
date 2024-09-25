class Solution:
    #TC: O(N^2) SC: O(N)
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        cnt = defaultdict(int)
        power = [1]* 1001
        mod = 10**9 + 7
        
        for i in range(1, 1001):
            power[i] = (power[i-1]* 37) % mod
            
        
        for word in words:
            hc = 0
            for i,c in enumerate(word):
                hc += (power[i+1] * (ord(c)- ord('a')+ 1)) % mod
                cnt[hc]+=1
                
        ans = [0]* len(words)
        for i,word in enumerate(words):
            hc = 0
            for j,c in enumerate(word):
                hc += (power[j+1] * (ord(c)- ord('a')+ 1)) % mod
                ans[i]+= cnt[hc]
                
        return ans
                
                
