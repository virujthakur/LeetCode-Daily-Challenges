# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC: O(N) SC: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p= None
        cnt= 0
        temp = head
        while temp:
            temp.prev= p
            p= temp
            temp= temp.next
            cnt+=1
            
        for i in range(cnt//2):
            if p.val != head.val:
                return False
            p= p.prev
            head= head.next
        
        return True
