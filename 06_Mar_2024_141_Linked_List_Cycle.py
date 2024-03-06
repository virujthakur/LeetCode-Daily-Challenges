# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        f= head
        s= head
        
        while f and s:
            if s:
                s= s.next
            if f:
                f= f.next
            if f:
                f= f.next
                
            if s==f:
                break
        return f==s and f 
