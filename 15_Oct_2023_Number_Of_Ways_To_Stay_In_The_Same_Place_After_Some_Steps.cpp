//TC: O(N * 2N) SC: O(N * 2N)
long long dp[500][1001];

class Solution {
public:
    int mod= 1e9+7;
    int recur(int diff, int steps, int& arrLen)
    {
        if(steps==0 && diff==0)
            return 1;
        
        if(steps==0) return 0;
        
        if(dp[diff][steps]!=-1) return dp[diff][steps];
            
        long long ans=0;
        if(diff+1 < arrLen)
        ans+= recur(diff+1, steps-1, arrLen)% mod;
        
        if(diff-1 >=0)
        ans+= recur(diff-1, steps-1, arrLen)% mod;
        
        ans+= recur(diff, steps-1, arrLen)% mod;
        
        return dp[diff][steps]= ans % mod;
    }
    
    int numWays(int steps, int arrLen) {
        
        memset(dp, -1 , sizeof(dp));
        return recur(0, steps, arrLen);
        
    }
};
