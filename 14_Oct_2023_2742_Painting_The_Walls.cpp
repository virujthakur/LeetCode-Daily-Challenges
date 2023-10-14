int dp[500][1001];

class Solution {
public:
    int recur(vector<int>& cost, vector<int>& time, int i, int occupied)
    {
        int n= cost.size();
        int ans= 1e9;
        
        if(occupied >= n-i)
            return 0;
        
        if(i==n)
            return 1e9;
        
        if(dp[i][occupied+n]!=-1) return dp[i][occupied+n];
        
        ans= min(ans, cost[i]+ recur(cost,time,i+1, occupied+ time[i]));
        ans= min(ans, recur(cost,time,i+1, occupied-1));
        
        return dp[i][occupied+ n]= ans;
        
    }
    
    int paintWalls(vector<int>& cost, vector<int>& time) {
        
        int n= cost.size();
        memset(dp, -1, sizeof(dp));
        
        return recur(cost, time, 0, 0);
    }
};
