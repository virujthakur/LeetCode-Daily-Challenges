# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC: O(N) SC: O(1)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        j = head
        
        previ= None
        
        while j:
            if j.next.val==0:
                    
                if previ is None:
                    head= j
                else:
                    previ.next= j
                    
                previ = j
                
                if j.next.next == None:
                    j.next= None
                    
                i= j.next
            else:
                j.next.val+= j.val
                
            j= j.next
            
        return head
                
            
                
