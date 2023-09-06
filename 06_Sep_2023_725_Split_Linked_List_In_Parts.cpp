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
    //TC: O(N*K) SC: O(1)
    int getSize(ListNode* head)
    {
        ListNode* cur= head;
        int sz=0;
        while(cur)
        {
            cur= cur->next;
            sz++;
        }
        
        return sz;
    }
    
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        
        int n= getSize(head);
        int partSize= n/k;
        int rem= n%k;
        vector<ListNode*> answer;
        
        ListNode* cur= head;
        ListNode* prev= NULL;
        for(int i=0; i<k;i++)
        {
            ListNode* partHead= cur;
            int ps= partSize;
            while(ps-- && cur)
            {
                prev= cur;
                cur= cur->next;
            }
            
            if(rem-->0 && cur)
            {
                prev= cur;
                cur= cur->next; 
            }
            
            if(prev && prev->next!= NULL)
                prev->next= NULL;
            
            answer.push_back(partHead);
        }
        
        return answer;
    }
};