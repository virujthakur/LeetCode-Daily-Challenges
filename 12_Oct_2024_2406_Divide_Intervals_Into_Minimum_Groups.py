class Solution:
    #TC: O(N) SC: O(N)
    def minGroups(self, intervals: List[List[int]]) -> int:
        prefix = [0]* (10**6 + 2)
        
        for st,en in intervals:
            prefix[st]+=1 
            prefix[en+1]-=1
        
        s = 0
        for i in range(10**6 + 2):
            s+= prefix[i]
            prefix[i] = s
            
        return max(prefix)
