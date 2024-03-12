# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC: O(N) SC:O(N)
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        dum = ListNode(-1, head)
        f= {}
        cur = dum
        while cur:
            s += cur.val
            
            if s in f:
                # print(cur.val)
                prev= f[s]
                cur= prev.next
                
                p = s+ cur.val
                while p != s:
                    del f[p]
                    cur= cur.next
                    p+= cur.val
            
            
                prev.next = cur.next
            
            else:
                f[s]= cur
            
            cur= cur.next
        return dum.next
            
