class Solution:
    #TC: O(2^N) SC: O(1)
    def RLE(self, s):
        ans = ''
        i ,j = 0,0
        cnt = 0
        while j< len(s):
            cnt +=1
            
            if s[j] != s[i]:
                ans += str(j-i) + s[i]
                i = j
                cnt = 1

            j+=1

        ans += str(j-i) + s[i]
        return ans

    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(n-1):
            ans = self.RLE(ans)
        
        return ans
