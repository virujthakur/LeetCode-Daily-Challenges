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
 //TC: O(N) SC: O(1)
class Solution {
public:
    int cur_dashes= 0;
    void preorder(TreeNode* root, string& traversal, int& j, int prev_dashes)
    {
        int num_dashes = 0;
        while(j< traversal.size() && traversal[j] == '-')
        {
            j++;
            num_dashes+=1;
        }

        cur_dashes= num_dashes;


        // cout<<root->val<<" "<<num_dashes<<" "<<prev_dashes<<endl;
        if (num_dashes > prev_dashes)
        {
            string node_left = "";
            while (j< traversal.size() && traversal[j]!= '-')
            {
                node_left.push_back(traversal[j]);
                j++;
            }

            TreeNode* left = new TreeNode(stoi(node_left));
            root->left = left;
            preorder(left, traversal, j, num_dashes);

            while(cur_dashes <= prev_dashes)
            {
                return;
            }

            if (j == traversal.size())
            {
                return;
            }

            string node_right = "";
            while (j< traversal.size() && traversal[j]!= '-')
            {
                node_right.push_back(traversal[j]);
                j++;
            }

            TreeNode* right = new TreeNode(stoi(node_right));
            root->right = right;
            preorder(right, traversal, j, num_dashes);

            if (j == traversal.size())
            {
                return;
            }
        }
    }

    TreeNode* recoverFromPreorder(string traversal) {
        string root_node = "";
        int j= 0;
        while (j< traversal.size() && traversal[j]!= '-')
        {
            root_node.push_back(traversal[j]);
            j++;
        }
        

        TreeNode* root = new TreeNode(stoi(root_node));
        preorder(root, traversal, j, 0);

        return root;
    }
};
