class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        
        set<string> ns ;
        for(auto s : nums)
            ns.insert(s) ;
        
        string ans ;
        string s ;
        solve(0,s,ns,ans) ;
        return ans ;
    }
    
    void solve(int i, string &s, set<string> &ns, string &ans)
    {
        if(ans.size() == ns.begin()->size())
        {
            return ;
        }
        
        if(i == ns.begin()->size())
        {
            if(ns.find(s) == ns.end())
            {
                ans = s ;
            }
            return ;
        }
        
        s = s + '0' ;
        solve(i+1, s, ns, ans) ;
        s.pop_back() ;
        s = s + '1' ;
        solve(i+1, s, ns, ans) ;
        s.pop_back() ;
    }
};
