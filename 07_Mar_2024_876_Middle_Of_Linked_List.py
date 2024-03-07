# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(N) SC: O(1)
        sz=0
        temp= head
        while temp:
            temp= temp.next
            sz+=1
        
        cnt=0
        while cnt < sz //2:
            head= head.next
            cnt+=1
        
        return head
