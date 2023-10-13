class Solution {
public:
    
    //TC: O(N) SC: O(N)
    
    int recur(vector<int>& cost, int i, vector<int>& dp)
    {
        int n= cost.size();
        
        if(i>=n) return 0;
        
        if(dp[i]!=-1) return dp[i];
        
        int ans1= cost[i] + recur(cost,i+1, dp);
        int ans2= cost[i] + recur(cost,i+2, dp);
        
        return dp[i]= min(ans1, ans2);
        
    }
    int minCostClimbingStairs(vector<int>& cost) {
        
        int n= cost.size();
        vector<int> dp(n,-1);
        
        int ans1= recur(cost, 0, dp);
        
        dp.resize(n,-1);
        
        int ans2= recur(cost, 1, dp);
        
        return min(ans1, ans2);
        
    }
};
