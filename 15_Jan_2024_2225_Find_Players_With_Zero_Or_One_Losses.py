class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses =defaultdict(int)
        losers = set()
        winners = set()
        
        for w,l in matches:
            losers.add(l)
            winners.add(w)
            losses[l]+=1
        
        ans0, ans1= set(),set()
        for w in winners:
            if w not in losers:
                ans0.add(w)
            if losses[w]==1:
                ans1.add(w)
        for l in losers:
            if losses[l]==1:
                ans1.add(l)
                
        return [sorted(list(ans0)),sorted(list(ans1))]
