//TC: O(N) SC: O(N)
class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        
        int n= groupSizes.size();
        
        vector<pair<int,int>> v;
        for(int i=0;i<n;i++)
        {
            v.push_back({groupSizes[i],i});
        }
        
        sort(v.begin(), v.end());
        vector<vector<int>> ans;
        
        for(int i=0;i<n;)
        {
            int sz= v[i].first;
            vector<int> grp;
            
            while(i<n && grp.size()< sz)
            {
                int person= v[i].second;
                grp.push_back(person);
                i++;
            }
            
            ans.push_back(grp);
        }
        
        return ans;
        
    }
};