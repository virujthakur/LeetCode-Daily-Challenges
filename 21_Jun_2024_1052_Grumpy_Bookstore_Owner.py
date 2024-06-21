class Solution:
    #TC: O(N) SC: O(1)
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n= len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i]== 0:
                ans+= customers[i]
                customers[i] = 0
                
        s = 0
        res = 0
        i =0
        for j in range(minutes-1):
            s+= customers[j]
            
        for j in range(minutes-1, n):
            s+= customers[j]
            res= max(res, s)
            s-= customers[i]
            i+=1
            
        return ans+res
            
                
        
