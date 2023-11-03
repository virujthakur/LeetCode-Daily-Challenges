class Solution {
public:
    // TC: O(N) SC: O(1)
    vector<string> buildArray(vector<int>& target, int n) {
        
        int m= target.size();
        vector<string> ans;
        int prev=0;
        
        for(int i=0; i< m; i++)
        {
            for(int j=0; j< target[i]- prev-1; j++)
            {
                ans.push_back("Push");
                ans.push_back("Pop");
            }
            
            ans.push_back("Push");
            prev= target[i];
        }
        
        return ans;
        
    }
};
