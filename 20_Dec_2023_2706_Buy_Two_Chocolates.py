class Solution:
    #TC: O(NLOGN) SC: O(1)
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        org_money= money
        cnt= 0
        if money- prices[0] >=0:
            money-= prices[0]
            cnt +=1
            
        if money- prices[1] >=0:
            money-= prices[1]
            cnt +=1
            
        if cnt != 2: return org_money 
        else: return money
        
