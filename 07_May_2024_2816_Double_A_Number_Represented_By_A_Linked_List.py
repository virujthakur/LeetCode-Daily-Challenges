# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #TC : O(N) SC: O(N)
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st= deque()
        temp = head
        while temp:
            st.append(temp)
            temp= temp.next
         
        c = 0
        while st:
            st[-1].val *= 2
            st[-1].val += c
            c = st[-1].val // 10
            
            st[-1].val %= 10
            st.pop()
            
        if c ==1:
            newHead = ListNode(1, head)
            return newHead
        else:
            return head
