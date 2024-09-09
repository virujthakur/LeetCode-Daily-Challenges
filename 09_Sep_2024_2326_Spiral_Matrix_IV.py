# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC: O(M*N) SC: O(M*N)
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1]* n for _ in range(m)]
        visited = [[False]* n for _ in range(m)]
        
        di = ((0,1), (1,0), (0, -1), (-1,0))
        curx, cury = 0,0
        d = 0
        
        while head:
            ans[curx][cury]= head.val
            visited[curx][cury]= True
            
            newx = curx + di[d][0]
            newy = cury + di[d][1]
            
            if newx >= m or newy >= n or newx < 0 or newy < 0 or visited[newx][newy]:
                d +=1
                d %=4
                
            newx = curx + di[d][0]
            newy = cury + di[d][1]
            
            curx = newx
            cury = newy
            head = head.next
            
        return ans
        
        
        
