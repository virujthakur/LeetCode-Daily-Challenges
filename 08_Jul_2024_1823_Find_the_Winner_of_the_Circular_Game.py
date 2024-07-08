class Solution:
    #TC: O(N) SC: O(1)
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1:
            return 1
        
        x= self.findTheWinner(n-1, k)
        return (x+k-1)% n + 1
