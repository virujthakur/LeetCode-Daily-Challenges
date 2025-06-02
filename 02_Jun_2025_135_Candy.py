class Solution:
    #TC: O(N) SC: O(N)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l,r = [1]*n , [1]* n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                l[i] = l[i-1] + 1
            
            if ratings[n-1-i] > ratings[n-1-i+1]:
                r[n-1-i] = r[n-1-i+1] + 1

        s = 0
        for i in range(n):
            s += max(l[i], r[i])

        return s
