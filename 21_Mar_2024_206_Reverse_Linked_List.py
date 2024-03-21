# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(N) SC: O(1)
        prev= None
        ans= None
        while head:
            nx= head.next
            head.next= prev
            prev= head
            if not nx:
                ans= head
            head= nx
            
        
        return ans
