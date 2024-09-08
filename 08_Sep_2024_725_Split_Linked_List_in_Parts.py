# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #TC : O(N) SC: O(1)
        def cntNodes(h):
            temp = h
            cnt = 0
            while temp:
                cnt +=1
                temp= temp.next
                
            return cnt
        
        n= cntNodes(head)
        
    
        partSize = n // k
        rem = n % k
        
        ans = []
        cnt = 0
        it = head
        
        while it:
            if cnt ==0:
                ans.append(it)
                
            if rem > 0:
                if cnt == partSize:
                    temp = it.next
                    it.next = None
                    it= temp
                    cnt = 0
                    rem -=1
                    continue
            else:
                if cnt == partSize -1:
                    temp = it.next
                    it.next = None
                    it= temp
                    cnt = 0
                    continue
                
            it = it.next
            cnt +=1
            
        while len(ans) < k:
            ans.append(None)
            
        return ans
            
            
            
            
