class Solution:
    #TC: O(N*2^N) SC: O(1)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans =[]
        t = re.findall(r'\d+|[\+\-\*/]', expression)
        for i, tok in enumerate(t):
            if tok not in ['+', '-', '*']:
                t[i]= int(tok)
                
        def recur(tokens):
            results = []
            if len(tokens) == 0:
                return results
            
            if len(tokens) == 1:
                return tokens
            
            for i,c in enumerate(tokens):
                if c in ['+', '-', '*']:
                    left = recur(tokens[:i])
                    right = recur(tokens[i+1:])
                    
                    for l in left:
                        for r in right:
                            if c == '+':
                                results.append(l+r)
                            elif c=='-':
                                results.append(l-r)
                            else:
                                results.append(l*r)
                                
            return results
                    
        return recur(t)
                    
                    
                    
