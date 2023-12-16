class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t= ''.join(sorted(t))
        s= ''.join(sorted(s))
        # print(s)
        # print(t)
        return t==s
