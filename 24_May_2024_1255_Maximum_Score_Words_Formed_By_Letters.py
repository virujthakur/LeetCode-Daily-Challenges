class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        #TC: O(2^N * LEN(letters)) SC: O(1)
        def get_score_character(a):
            return score[ord(a)- ord('a')]
        
        n= len(words)
        ans = 0
        
        for i in range(1<<n):
            score_subset = 0
            f= defaultdict(int)
            for l in letters:
                f[l]+=1
                
            flag= True
            
            for j in range(n):
                if not flag:
                    break
                    
                if (1<<j)& i:
                    for c in words[j]:
                        f[c]-=1
                        if f[c] < 0:
                            flag= False
                            break
                        score_subset+= get_score_character(c)
                            
            if flag:
                ans = max(ans, score_subset)
                
        return ans
        
        
        
