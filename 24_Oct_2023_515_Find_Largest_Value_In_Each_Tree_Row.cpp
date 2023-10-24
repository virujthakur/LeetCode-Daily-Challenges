/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    //TC: O(N) SC: O(N)
    vector<int> largestValues(TreeNode* root) {
        
        if(!root) return {};
        queue<TreeNode*> q;
        
        q.push(root);
        vector<int> ans;
        
        int level=-1;
        while(!q.empty())
        {
            level++;
            int sz= q.size();
            int mx= INT_MIN;
            
            for(int i=0; i<sz; i++)
            {
                auto x= q.front();
                q.pop();
                mx= max(mx, x->val);
                if(x->left) q.push(x->left);
                if(x->right) q.push(x->right);
            }
            
            ans.push_back(mx);
            
        }
        
        return ans;
        
    }
};
