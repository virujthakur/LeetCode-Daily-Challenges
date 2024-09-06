# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC : O(N) SC : O(N)
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        prev = None
        pointer= head
        
        while pointer:
            if pointer.val in nums:
                if prev==None:
                    head= pointer.next
                    pointer= pointer.next
                    continue
                else:
                    prev.next= pointer.next
                    pointer= pointer.next
                    continue
                    
                    
            prev= pointer        
            pointer= pointer.next
            
        return head
                
