class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        
        vector<int> dp(high+1);
        int mod= 1e9+7;
        
        dp[0]=1;
        
        for(int i=0;i<=high;i++)
        {
            if(i+zero<= high)
            dp[i+zero]+= (dp[i] %mod);
            
            if(i+one<=high)
            dp[i+one]+=  (dp[i] %mod);
        }
        
        long long ans=0;
        for(int i= low; i<= high; i++)
        {
            ans+= (dp[i]% mod);
        }
        
        return ans % mod;
    }
};
