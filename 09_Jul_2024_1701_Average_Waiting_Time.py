class Solution:
    #TC: O(N) SC: O(1)
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        s = 0
        busy_till = 0
        for c in customers:
            if busy_till < c[0]:
                busy_till = c[0]+ c[1]
                s+= c[1]
            else:
                wt= busy_till- c[0]
                wt+= c[1]
                s+= wt
                busy_till+= c[1]
               
        # print(s)
        return s/n
                
            
                
            
