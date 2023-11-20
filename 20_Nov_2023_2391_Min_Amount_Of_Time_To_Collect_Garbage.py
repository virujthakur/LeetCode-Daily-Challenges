class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n= len(garbage)
        p = 0
        m = 0
        g = 0
        poff = 0
        moff = 0
        goff = 0
        
        for i in range(n):
            ga= garbage[i]
            for c in ga :
                if c == 'G':
                    g= i
                    goff +=1
                elif c == 'M' :
                    m= i
                    moff +=1
                else :
                    p= i
                    poff +=1
        
        suffixTravel = [0]* (n-1)
        sum= 0
        i = 0
        for num in travel :
            sum+= num
            suffixTravel[i]= sum
            i+=1
           
        ans = 0
        ans += (poff + goff + moff)
        if g-1 >= 0:
            ans += suffixTravel[g-1]
        if p-1 >=0 :
            ans+= suffixTravel[p-1]
        if m-1 >=0 :
            ans+= suffixTravel[m-1]
            
        return ans
        
