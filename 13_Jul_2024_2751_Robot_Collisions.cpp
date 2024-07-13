class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        //TC: O(NLOGN) SC: O(N)
        multiset<int, greater<int>> right;
        multiset<int> left;
        int n= positions.size();
        unordered_map<int,int> hp;
        unordered_map<int,int> index;
        for(int i=0; i<n; i++)
        {
            if(directions[i]== 'L')
                left.insert(positions[i]);
            else
                right.insert(positions[i]);
            
            hp[positions[i]]= healths[i];
            index[positions[i]]= i;
        }
        
        vector<int> ans(n);
        while(right.size() > 0)
        {
            auto r_it= right.begin();
            int r= *r_it;
            
            auto l_it = left.upper_bound(r);
            if(l_it == left.end())
            {
                ans[index[r]]= hp[r];
                right.erase(r_it);
                continue;
            }
            
            int l= *l_it;
            int hr = hp[r];
            int hl= hp[l];
            
            if(hl > hr)
            {
                hp[l]-=1;
                right.erase(r_it);
                
            }
            else if(hr > hl)
            {
                hp[r]-=1;
                left.erase(l_it);
            }
            else
            {
                left.erase(l_it);
                right.erase(r_it);
            }
        }
        
        for(auto l: left)
        {
            ans[index[l]]= hp[l];
        }
        
        vector<int> result;
        for(auto a: ans)
        {
            if(a > 0)
                result.push_back(a);
        }
        return result;
    }
};
