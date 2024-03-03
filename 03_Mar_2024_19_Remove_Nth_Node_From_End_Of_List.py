# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#TC: O(SZ) SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp= head
        sz=0
        while temp:
            temp= temp.next
            sz+=1
            
        i=0
        prev= ListNode(-1)
        cur= head
        while i< (sz-n):
            prev= cur
            cur= cur.next
            i+=1

        prev.next= cur.next
        return head if n < sz else prev.next
