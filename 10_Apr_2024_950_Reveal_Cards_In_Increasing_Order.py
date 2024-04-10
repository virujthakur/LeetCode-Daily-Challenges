class Solution:
    #TC: O(NLOGN SC: O(1))
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n= len(deck)
        deck.sort()
        
        indices= [_ for _ in range(n)]
        order = []
        
        d= deque(range(n))
        
        while d:
            order.append(d[0])
            d.popleft()
            if not d:
                break
            d.append(d.popleft())
            
        # print(order)
        ans = [-1]* n
        for i in range(n):
            ans[order[i]]= deck[i]
            
        
        return ans
