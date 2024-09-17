class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        #TC: O(N*N) SC: O(N)
        words1 , words2 = s1.split(' '), s2.split(' ')
        ans = set()
        f1, f2 = defaultdict(int), defaultdict(int)
        for word in words1:
            f1[word]+=1
            
        for word in words2:
            f2[word]+=1
        
        for word in words1:
            if word not in words2 and f1[word] == 1:
                ans.add(word)
                
        for word in words2:
            if word not in words1 and f2[word] == 1:
                ans.add(word)
                
        return list(ans)
