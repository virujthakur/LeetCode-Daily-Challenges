# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC: O(N) SC: O(1)
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1= list1
        i=0
        while i< b:
            h1= h1.next
            i+=1
            
        h2= list2
        while h2.next:
            h2= h2.next
        
        h2.next= h1.next
        h1.next= None
        
        i= 0
        h1= list1
        while i< a-1:
            h1= h1.next
            i+=1
            
            
        h1.next= list2
        
        return list1
