class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime = [2,3,5,7]
        mod = 10**9 + 7
        # half postions have 4 possibilities
        # half positions have 5 posibilities

        def binExp(a, b):
            ans = 1
            while b > 0:
                if b%2 :
                    ans *= a
                    ans %= mod
                    b -=1
                else:
                    a= (a*a) % mod
                    b //=2
            
            return ans

        # print(binExp(4, n//2))
        # print(binExp(5, n//2 + n%2))
        return (binExp(4, n//2) % mod * binExp(5, n//2 + n%2) % mod) % mod

        
        
