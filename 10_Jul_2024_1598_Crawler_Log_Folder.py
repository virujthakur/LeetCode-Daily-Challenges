class Solution:
    #TC: O(N) SC: O(1)
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == '../':
                ans-=1
                ans = max(ans, 0)
            elif log== './':
                continue
            else:
                ans+=1
                
        return max(0, ans)
            
