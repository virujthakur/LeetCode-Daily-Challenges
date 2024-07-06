class Solution:
    #TC: O(TIME) SC: O(1)
    def passThePillow(self, n: int, time: int) -> int:
        while time:
            for i in range(1,n):
                time-=1
                if time == 0:
                    return i+1
                
            for i in range(n-2, -1, -1):
                time-=1
                if time==0:
                    return i+1
                
            
        return -1
