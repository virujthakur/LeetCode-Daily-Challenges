class Solution:
    #TC: O(N) SC: O(N)
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(a)- ord(b)) for a,b in zip(s, t)]
        # print(diff)
        n= len(diff)
        ans = 0
        j= 0
        curCost= 0
        for i in range(n):
            curCost+= diff[i]
            if curCost <= maxCost:
                ans= max(ans, i-j+1)
                
            while j<=i and curCost> maxCost:
                curCost-= diff[j]
                j+=1
                
            # print(j,i,curCost)
                
        return ans
            
