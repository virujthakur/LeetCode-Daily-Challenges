class Solution:
    #TC: O(N) SC: O(1)
    def checkValidString(self, s: str) -> bool:
        st= deque()
        n= len(s)
        
        flag= [True]* n
        for i, c in enumerate(s):
            if c== '(':
                st.append([c, i])
            elif c== ')':
                if st:
                    flag[st[-1][1]]= False
                    flag[i]= False
                    st.pop()
                    
        unb = ''
        for i in range(n):
            if flag[i]:
                unb += s[i]
                
        # print(unb)
        i = 0
        str_cnt= 0
        while i< len(unb) and unb[i] != '(':
            if unb[i] =='*':
                str_cnt+=1
            else:
                if not str_cnt:
                    return False
                else:
                    str_cnt-=1
            i+=1
        
        i=len(unb)-1 
        
        str_cnt= 0
        while i>=0 and unb[i] != ')':
            if unb[i] =='*':
                str_cnt+=1
            else:
                if not str_cnt:
                    return False
                else:
                    str_cnt-=1
            i-=1
            
        return True
            
            
        
        
                    
        
