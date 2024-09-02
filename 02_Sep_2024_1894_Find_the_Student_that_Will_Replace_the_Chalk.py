class Solution:
    #TC : O(N) SC: O(1)
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        s = sum(chalk)
        
        complete = k//s
        k -= complete * s
        
        for i in range(n):
            if k < chalk[i]:
                return i
            k-= chalk[i]
            
        return 0
