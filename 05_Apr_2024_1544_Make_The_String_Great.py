class Solution:
    #TC: O(N) SC: O(N)
    def makeGood(self, s: str) -> str:
        st = deque()
        # print(ord('a'))
        # print(chr(ord('a')- 32))
        for c in s:
            if st and (st[-1] == chr(ord(c)+ 32) or st[-1]== chr(ord(c)- 32)):
                st.pop()
                continue
            else:
                st.append(c)
                
        return ''.join(st)
