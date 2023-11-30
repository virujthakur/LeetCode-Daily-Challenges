import math
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n: return 0
        
        msb= 0
        for i in range (32):
            if(n & (1<<i)):
                msb= i
        
        return 2** (msb+1) - 1 - self.minimumOneBitOperations(n ^ (1<<msb))
