class Solution:
    #TC: O(N) SC: O(N)
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        ans = ''
        for i,c in enumerate(s):
            if i in spaces:
                ans += ' ' + c
            else:
                ans += c
                
        return ans
