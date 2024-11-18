class Solution:
    #TC: O(N*K) SC: O(1)
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code + code + code
        newcode = [0] * n
        
        for i in range(n, 2*n):
            s = 0
            
            if k > 0:
                for j in range(i+1, i+k+1):
                    s+= code[j]
                    
                newcode[i-n] = s
                
            elif k < 0 :
                for j in range(i-1, i+k-1, -1):
                    s+= code[j]
                    
                newcode[i-n] = s
                
            else:
                newcode[i-n] = 0
                
        return newcode
