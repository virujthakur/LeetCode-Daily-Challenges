class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s= list(s)
        d= defaultdict(str)
        
        n= len(s)
        used= set()
        for i in range(n):
            if s[i] not in d and t[i] in used:
                return False
            d[s[i]]= t[i]
            used.add(t[i])
        
        
        for i in range(n):
            s[i]= d[s[i]]
            
        # print(s,t)
        s= ''.join(s)
        return s==t
