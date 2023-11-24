class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n= len(piles)
        piles.sort()
        alex= n-1
        bob = 0
        score = 0
        while(bob < alex):
            score+= piles[alex-1]
            bob+=1
            alex-=2
        
        return score
        
