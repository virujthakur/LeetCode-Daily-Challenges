# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        #TC: O(N) SC: O(1)
        firstCp= -1
        prevCp= -1
        j= head
        p = None
        idx = 0
        
        minDistance = 10**9
        
        while j!= None:
            # print(idx)
            if p and j.val > p.val and j.next and j.next.val < j.val:
                curCp = idx
                if prevCp == -1:
                    firstCp = idx
                else:
                    minDistance = min(curCp-prevCp, minDistance)
                    
                prevCp= curCp
            
            if p and j.val < p.val and j.next and j.next.val > j.val:
                curCp = idx
                if prevCp == -1:
                    firstCp = idx
                else:
                    minDistance = min(curCp-prevCp, minDistance)
                    
                prevCp= curCp
            
            p= j
            j= j.next
            idx+=1
            
        if prevCp== firstCp:
            return [-1,-1]

        return [minDistance, prevCp- firstCp]
            
