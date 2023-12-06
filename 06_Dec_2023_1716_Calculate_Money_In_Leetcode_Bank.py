class Solution:
    def totalMoney(self, n: int) -> int:
        prevMonday=0
        prevDay=0
        ans= 0
        
        for i in range(n):
            if i%7 == 0:
                ans+= prevMonday+1
                prevMonday+=1
                prevDay= prevMonday
            else :
                ans+= prevDay+1
                prevDay+=1
                
        
        return ans
