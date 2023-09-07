/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    //TC: O(N) SC: O(1)
    ListNode* reverseBetween(ListNode* head, int l, int r) {
        
        int count=1;
        
        ListNode* cur= head;
        ListNode* prev= NULL;
        ListNode* L1= NULL;
        ListNode* L= NULL;
        ListNode* R= NULL;
        ListNode* R1= NULL;
        
        while(cur && count<=r)
        {
            // cout<<cur->val<<endl;
            if(count<l)
            {
                if(count== l-1)
                    L1= cur;
                
                count++;
                prev= cur;
                cur= cur->next;
            }
            else
            {
                if(count==l)
                {
                    L= cur;
                }
                
                if(count== r)
                {
                    R= cur;
                    R1= cur->next;
                }
                
                ListNode* temp= cur->next;
                cur->next= prev;
                prev= cur;
                cur= temp;
                count++;
            }
        }
        
        if(L1)
        {
            L1->next= R;
        }
        else
        {
            head= R;
        }
        
        L->next= R1;
        return head;
        
    }
};