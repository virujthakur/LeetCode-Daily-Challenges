class Solution:
    #TC: O(NLOGN) SC: O(1)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n= len(tokens)
        tokens.sort()      
        
        i,j= 0, n-1
        ans, score= 0,0
        while i<=j:
            if power>= tokens[i]:
                power-= tokens[i]
                score+=1
                i+=1
                ans= max(ans,score)
            elif score > 0:
                power+= tokens[j]
                j-=1
                score-=1
            else:
                break
        return ans
