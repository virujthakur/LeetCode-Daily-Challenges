class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n= len(s)
        l = s[:n//2]
        r = s[n//2:n]
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        c1= 0
        c2= 0
        for c in l:
            if c in vowels:
                c1+=1
        
        for c in r:
            if c in vowels:
                c2+=1
        
        return c1==c2
