/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

//TC: O(N) SC: O(1) Tortoise and Hare
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        ListNode* fast = head;
        ListNode* slow = head;
        
        while(fast!= NULL && fast->next!= NULL)
        {
            slow= slow->next;
            fast= fast->next;
            
            if(fast->next)
                fast= fast->next;
            else
                return false;
            
            if(slow == fast)
                return true;
        }
        
        return false;
        
    }
};