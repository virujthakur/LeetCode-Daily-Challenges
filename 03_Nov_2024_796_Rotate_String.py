class Solution:
    #TC: O(N^2) SC: O(1)
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n+1):
            s = s[1:]+ s[0]
            if s == goal:
                return True
            
        return False
