int dp[200000+1];
class Solution {
public:
    int recur(vector<int>& nums, int sum)
    {
        if(sum==0)
            return 1;
        if(sum<0)
            return 0;
        
        if(dp[sum]!=-1) return dp[sum];
        
        int ans=0;
        for(int i=0;i<nums.size();i++)
            ans+= recur(nums, sum-nums[i]);
        
        return dp[sum]= ans;
        
    }
    
    int combinationSum4(vector<int>& nums, int target) {
        
        memset(dp,-1,sizeof(dp));
        return recur(nums,target);
    }
};