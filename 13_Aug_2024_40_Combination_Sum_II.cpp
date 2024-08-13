class Solution {
public:
    //TC: (2^N) SC: O(1)
    vector<vector<int>> ans;
    void recur(vector<int>& dis, int idx, int t, int& target, vector<int> seq, map<int,int>& f)
    {
        int n= dis.size();
        if (t>=31)
            return;
        
        if(idx == n)
        {
            if(t== target)
                ans.push_back(seq);
                
            return;
        }
        
        int t_sum = 0;
        for(int i=0; i<f[dis[idx]]+1; i++)
        {
            recur(dis, idx+1, t+ t_sum, target, seq, f);
            seq.push_back(dis[idx]);
            t_sum+= dis[idx] ;
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        map<int,int> f;
        for(auto c: candidates)
            f[c]+=1;
            
        vector<int> dis;
        for(auto x: f)
            dis.push_back(x.first);
            
        recur(dis, 0, 0, target, {}, f);
        return ans;
        
    }
};
