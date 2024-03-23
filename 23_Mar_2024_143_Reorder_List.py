# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
   #TC: O(N) SC: O(N)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp= head
        st = deque()
        while temp:
            st.append(temp)
            temp= temp.next
        
        f= head
        n= len(st)
        for i in range(n//2):
            nx= f.next
            f.next= st[-1]
            if n%2==0 and i== (n//2 -1):
                st[-1].next= None
                break
            st[-1].next= nx
            st.pop()
            f= nx
            
        if n%2:
            f.next= None
            
