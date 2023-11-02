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
    unordered_map<TreeNode*, int> count;
    unordered_map<TreeNode*, int> sum;
    
    int dfsCount(TreeNode* root)
    {
        if(!root) return 0;
        
        int l= dfsCount(root->left);
        int r= dfsCount(root->right);
        return count[root]= l+ r+1;
    }
    
    int ans=0;
    int dfsSum(TreeNode* root)
    {
        if(!root) return 0;
        
        int l= dfsSum(root->left);
        int r= dfsSum(root->right);
        
        
        sum[root]= l+ r+ root->val;
        if(sum[root]/ count[root]== root->val)
            ans++;
        
        return sum[root];
        
    }
    int averageOfSubtree(TreeNode* root) {
        
        dfsCount(root);
        dfsSum(root);
        
        return ans;
    }
};
