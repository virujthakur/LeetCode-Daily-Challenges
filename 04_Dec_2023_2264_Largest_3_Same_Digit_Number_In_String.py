class Solution:
    #TC: O(N) SC: O(1)
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        
        for i in range(2, n):
            temp= num[i-2: i+1]
            d= Counter(temp)
            if len(d) == 1 : 
                ans= max(ans, temp)
        
        return ans
