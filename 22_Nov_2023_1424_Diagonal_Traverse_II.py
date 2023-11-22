from collections import deque
class Solution:
    #TC: O(N) SC: O(N)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n= len(nums)
        m = 0
        for numList in nums:
            m= max(len(numList), m)
            
        d = [(1, 0), (0, 1)]
        q= deque()
        ans= []
        vis = set()
        
        q.append((0,0))
        ans.append(nums[0][0])
        vis.add((0,0))
        
        level = 0
        while q :
            sz = len(q)
            for i in range(sz):
                curX, curY = q[0]
                
                q.popleft()
                for x,y in d :
                    newX= x+ curX
                    newY= y+ curY
                    
                    if newX < n and newY < len(nums[newX]) and (newX,newY) not in vis:
                        q.append((newX, newY))
                        ans.append(nums[newX][newY])
                        vis.add((newX,newY))
        
        return ans         
