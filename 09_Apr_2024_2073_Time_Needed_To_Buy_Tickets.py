class Solution:
    #TC: O(N^2) SC O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k]:
            for i,t in enumerate(tickets):
                if tickets[i] > 0:
                    tickets[i]-=1
                    ans+=1
                if tickets[k] == 0:
                    break
                # print(tickets)
                    
        return ans

    #TC: O(N) SC O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i,t in enumerate(tickets):
            if i<=k:
                ans+= min(t, tickets[k])
            else:
                ans+= min(t, tickets[k]-1)
                
        return ans
            
