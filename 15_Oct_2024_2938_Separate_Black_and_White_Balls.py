class Solution:
    #TC: O(N) SC: O(1)
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        s = list(s)
        ans = 0
        prev = -1
        for i in range(n):
            if s[i] == '0':
                # print(i, prev)
                ans += i-prev-1
                prev+=1
                
        return ans
                
