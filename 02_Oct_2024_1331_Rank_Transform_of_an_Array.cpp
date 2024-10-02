class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n= arr.size();
        map<int,vector<int>> f;
        for(int i=0; i<n; i++)
            f[arr[i]].push_back(i);
            
        vector<int> rank(n, -1);
        int cnt = 1;
        for(auto x: f)
        {
            for(auto y: x.second)
                rank[y]= cnt;
                
            cnt+=1;
        }
        return rank;
    }
};
