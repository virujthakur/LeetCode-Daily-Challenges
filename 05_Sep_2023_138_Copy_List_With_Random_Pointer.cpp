/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

//TC: O(N) SC: O(N)
class Solution {
public:
    Node* copyRandomList(Node* head) {
        
        Node* cur= head;
        Node* prev= NULL;
        Node* newHead;
        map<Node*,Node*> randStore;
        map<Node*,Node*> org;
        while(cur)
        {
            Node* newNode= new Node(cur-> val);
            
            if(!newHead)
            {
                newHead= newNode;
            }
            
            if(prev!= NULL)
            {
                prev->next= newNode;
            }
            
            randStore[newNode]= cur->random;
            org[cur]= newNode;
            cur= cur->next;
            prev= newNode;
        }
        
        cur= newHead;
        
        while(cur)
        {
            cur->random= org[randStore[cur]];
            cur= cur->next;
        }
        
        return newHead;
        
    }
};