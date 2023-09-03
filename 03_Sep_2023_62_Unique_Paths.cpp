int dp[101][101];

//TC: O(N*M) SC: O(N*M)
class Solution {
public:
    int dfs(int i, int j, int& m, int& n)
    {
        if(i<0 || j<0 ||i>=m || j>=n)
            return 0;
        
        if(i==m-1 && j==n-1)
            return 1;
        
        if(dp[i][j]!=-1) return dp[i][j];
        
        int ans=0;
        ans+= dfs(i+1,j,m,n);
        ans+= dfs(i,j+1,m,n);
        return dp[i][j]= ans;
    }
    
    int uniquePaths(int m, int n) {
        
        memset(dp, -1, sizeof(dp));
        return dfs(0,0,m,n);
    }
};