class Solution:
    #TC: O(N) SC: O(N)
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt = 0
        s = 0
        for i in range(1,n+1):
            if s+ i > maxSum:
                break
                
            if i in banned:
                continue
        
            s+= i
            # print(i)
            cnt +=1
        
        # print(s)
        return cnt
