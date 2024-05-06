# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(N) SC: O(N)
        st = deque()
        temp= head
        while temp:
            
            while st and st[-1].val < temp.val:
                st.pop()
                
            if (st):
                st[-1].next = temp
            else:
                head = temp
            
            st.append(temp)
            temp= temp.next
            
        return head
