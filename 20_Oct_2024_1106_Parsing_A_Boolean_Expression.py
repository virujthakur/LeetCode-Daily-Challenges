class Solution:
    #TC: O(2*N) SC: O(N)
    def parseBoolExpr(self, expression: str) -> bool:
        expression = list(expression)
        st = deque()
        
        for i,c in enumerate(expression):
            if c == 'f':
                expression[i] = False
            elif c == 't':
                expression[i] = True
        
        for i,c in enumerate(expression):
            if c == ')':
                op = None
                operands = []
                
                while len(st) > 0 and st[-1] != '(':
                    o = st[-1] 
                    if type(o)== bool:
                        operands.append(o)
                    st.pop()
                   
                if len(st) > 0 and st[-1] == '(':
                    st.pop() 
                    
                op = st[-1]
                st.pop()
                ans = None
                
                # print(operands, op)
                for o in operands :
                    if op == '&':
                        if ans == None:
                            ans = o
                        else:
                            ans &= o
                    elif op == '|':
                        if ans == None:
                            ans = o
                        else:
                            ans |= o
                    elif op == '!':
                        ans = not o
                            
                st.append(ans)
        
            else:
                st.append(c)
           
        
        return st[-1]
                    
                        
                
