class Solution {
public:
    // TC: O(N*N*9) SC: O(1)
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n= grid.size();
        vector<vector<int>> ans(n-2, vector<int>(n-2));
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {   
                if(i+3<=n and j+3 <=n)
                {
                    int mxVal= 0;
                    for(int x=i; x<i+3; x++)
                    {
                        for(int y= j; y<j+3; y++)
                        {
                            mxVal= max(mxVal, grid[x][y]);
                        }
                    }
                    
                    ans[i][j]= mxVal;
                }
            }
        }
        
        return ans;
        
    }
};
