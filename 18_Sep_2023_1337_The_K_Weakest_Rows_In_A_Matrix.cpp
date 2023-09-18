class Solution {
public:
    //TC: O(N*M + NLOGN) SC: O(N)
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int n= mat.size();
        int m= mat[0].size();
        
        vector<pair<int,int>> v;
        for(int i=0; i<n; i++)
        {
            int countOnes=0;
            for(int j=0; j<m; j++)
            {
                if(mat[i][j]==1)
                    countOnes++;
            }
            v.push_back({countOnes,i});
        }
        
        sort(v.begin(),v.end());
        vector<int> answer;
        for(int i=0; i<k; i++)
            answer.push_back(v[i].second);
        
        return answer;
    }
};
