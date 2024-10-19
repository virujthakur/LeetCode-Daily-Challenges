class Solution:
    #TC: O(N^2) SC: O(1)
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(x):
            return x[::-1]
        
        def invert(x):
            x = list(x)
            for i in range(len(x)):
                if x[i]== '0':
                    x[i] = '1'
                else:
                    x[i] = '0'
                    
            return ''.join(x)
                    
            
        prev = '0'
        for i in range(n-1):
            prev = prev + '1' + reverse(invert(prev))
        
        # print(prev)
        return prev[k-1]
            
        
            
