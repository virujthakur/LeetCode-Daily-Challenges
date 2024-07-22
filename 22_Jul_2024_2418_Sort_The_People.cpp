class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int,string> mp ;
        int n = heights.size() ;
        
        for(int i = 0 ; i < n ; i++)
        {
            mp[heights[i]] = names[i] ;
        }
        
        vector<string> ans ;
        
        for(auto i : mp)
            ans.push_back(i.second) ;
        
        reverse(ans.begin(), ans.end());
        
        return ans ;
    }
};
