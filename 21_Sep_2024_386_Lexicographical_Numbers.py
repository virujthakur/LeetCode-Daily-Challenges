class Solution:
    #TC: O(N) SC: O(1)
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        
        def recur(current):
            if current > n:
                return
            
            ans.append(current)
            
            for j in range(10):
                next_number = current * 10+ j
                if next_number <= n:
                    recur(next_number)
        
        for i in range(1,10):
            recur(i)
            
            
        return ans
    
        
            
        
        
