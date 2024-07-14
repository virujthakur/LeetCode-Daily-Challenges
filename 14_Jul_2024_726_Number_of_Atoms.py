class Solution:
    #TC: O(N^2) SC: O(N)
    def countOfAtoms(self, formula: str) -> str:
        formula = f'({formula})'
        n= len(formula)
        st= deque()
        ans = defaultdict(int)
        
        def isDigit(c):
            if ord('0') <= ord(c) <= ord('9'):
                return True
            return False
        
        def isLowerCase(c):
            if ord('a') <= ord(c) <= ord('z'):
                return True
            return False
        
        def isUpperCase(c):
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            return False
        
        i=0
        while i < len(formula):
            
            element = formula[i]
            if element == '(':    
                st.append((element, 1))
                i+=1
                continue
                
            j= i+1
            while j<n and isLowerCase(formula[j]):
                element+= formula[j]
                j+=1
            
            i=j
            
            num = ''
            
            j= i
            while j< n and isDigit(formula[j]):
                num+= formula[j]
                j+=1
                
            if num== '':
                num= '1'
            
            i=j
            # print(element, num, i, j)
            
            if element != ')':
                st.append((element, int(num)))
                continue
            
            if element == ')':
                popped_elements= []
                while st and st[-1][0] != '(':
                    f = st[-1][1]
                    popped_elements.append((st[-1][0], f* int(num)))
                    st.pop()
                    
                st.pop()
                    
                for ele in reversed(popped_elements):
                    st.append(ele)
           
        while st:
            ans[st[-1][0]]+= st[-1][1]
            st.pop()
            
        
        v =[]
        for k,val in ans.items():
            v.append((k, val))
            
        v.sort()
        res = ''
        for a in v:
            res+= a[0]
            if a[1]> 1:
                res+= str(a[1])
                
        return res
                    
                    
                
                
                
            
        
