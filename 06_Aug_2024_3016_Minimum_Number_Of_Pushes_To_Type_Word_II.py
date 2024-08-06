class Solution:
    #TC: O(N) SC: O(N)
    def minimumPushes(self, word: str) -> int:
        f= defaultdict(int)
        for c in word:
            f[c]+=1
           
        # print(f)
        f = list(f.items())
        f.sort(key = lambda x: x[1], reverse= True)
        # print(f)
        
        cost = 1
        ans = 0
        count = 0
        
        for c in f:
            ans+= cost * c[1]
            count+=1
            if count==8:
                count =0
                cost+=1
        
        return ans
            
