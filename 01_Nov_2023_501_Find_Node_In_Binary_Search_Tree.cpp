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
    unordered_map<int,int> freq;
    void preOrder(TreeNode* root)
    {
        if(!root) return;
        
        freq[root->val]++;
        preOrder(root->left);
        preOrder(root->right);
    }
    vector<int> findMode(TreeNode* root) {
        
        preOrder(root);
        
        int mxFreq= 0;
        vector<int> ans;
        for(auto x: freq)
        {
            mxFreq= max(mxFreq, x.second);
        }
        
        for(auto x: freq)
        {
            if(x.second == mxFreq)
                ans.push_back(x.first);
        }
        
        return ans;
        
    }
};
