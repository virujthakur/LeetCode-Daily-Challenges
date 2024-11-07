//TC: O(24*N) SC: O(1)
class Solution {
public:
    int recur(int idx, int bitPos, vector<int>& nums, vector<int>& dp) 
    {
        if (idx == nums.size()) return 0;

        if (dp[idx] != -1) return dp[idx];

        int ans = recur(idx + 1, bitPos, nums, dp);
        if ((1 << bitPos) & nums[idx]) {
            ans = max(ans, 1 + recur(idx + 1, bitPos, nums, dp));
        }

        return dp[idx] = ans;
    }
    
    int largestCombination(vector<int>& nums) {
        int n = nums.size();

        int ans = 0;
        for (int i = 0; i < 24; ++i) {
            vector<int> dp(n, -1); 
            ans = max(ans, recur(0, i, nums, dp));
        }

        return ans;
    }
};
