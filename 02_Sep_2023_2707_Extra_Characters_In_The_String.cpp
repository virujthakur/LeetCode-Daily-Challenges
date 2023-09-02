class Solution {
public:
    
    //TC: O(N)  SC: O(N)
    vector<int> dp;
    int recur(string& s, int i, unordered_map<string,bool>& mp)
    {
        if(i==s.size())
            return 0;
        
        if(dp[i]!=-1) return dp[i];
        
        string temp;
        int ans=1e9;
        for(int j=i; j<s.size(); j++)
        {
            temp.push_back(s[j]);
            if(mp[temp])
            {
                ans= min(ans, recur(s,j+1,mp));
            }
        }
        
        ans= min(ans, 1+ recur(s,i+1,mp));
        
        return dp[i]= ans;
    }
    
    int minExtraChar(string s, vector<string>& dictionary) {
        
        unordered_map<string,bool> mp;
        for(auto s: dictionary)
            mp[s]= true;
        
        dp.resize(s.size(),-1);
        
        return recur(s, 0, mp);
    }
};