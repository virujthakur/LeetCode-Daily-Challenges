# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC: O(N) SC: O(1)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        it = head.next
        prev = head
        
        while it:
            g = math.gcd(it.val, prev.val)
            gcd_node = ListNode(g, it)
            prev.next = gcd_node
            
            prev = it
            it = it.next
            
        return head
            
            
