class Solution:
    #TC: O(64) SC: O(64)
    def minEnd(self, n: int, x: int) -> int:
        def pad(x):
            diff = 64 - len(x)
            return '0'* diff + x
        
        bits_x = bin(x)[2:]
        bits_x = list(pad(bits_x))
        
        n -=1
        bits_n = list(bin(n)[2:])
        
        # print(bits_x)
        # print(bits_n)
        
        j= len(bits_x)-1
        for i in range(len(bits_n)-1, -1, -1):
            while bits_x[j] == '1':
                j-=1
                
            bits_x[j] = bits_n[i]
            j-=1
            
        return int(''.join(bits_x), 2)
            
        
