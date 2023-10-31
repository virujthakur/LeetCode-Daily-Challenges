class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        
        vector<int> ans;
        
        ans.push_back(pref[0]);
        
        int prev= pref[0];
        for(int i=1;i<pref.size();i++)
        {
            ans.push_back(pref[i]^prev);
            prev= prev^ ans[i];
        }
        
        return ans;
        
    }
};
