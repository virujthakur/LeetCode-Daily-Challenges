from collections import deque
class Solution:
    #TC: O(N) SC: O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        n= len(tokens)
        st= deque()
        ops= {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                if len(st) >= 2:
                    if t == '+':
                        new = st[-1] + st[-2]
                        st.pop()
                        st.pop()
                        st.append(new)
                    elif t== '-':
                        new = st[-2] - st[-1]
                        st.pop()
                        st.pop()
                        st.append(new)
                    elif t== '*':
                        new = st[-1] * st[-2]
                        st.pop()
                        st.pop()
                        st.append(new)
                    else:
                        new = st[-2] / st[-1]
                        if new < 0 :
                            new= ceil(new)
                        else:
                            new= floor(new)
                        st.pop()
                        st.pop()
                        st.append(new)
                    # print(st, t)
            else:
                st.append(int(t))
        
        return st[0]
