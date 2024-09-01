class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        #TC : O(N) SC: O(1)
        it = 0
        ans = [[-1]* n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if it == len(original):
                    return []
                ans[i][j]= original[it]
                it+=1
          
        if it != len(original):
            return []
        return ans
