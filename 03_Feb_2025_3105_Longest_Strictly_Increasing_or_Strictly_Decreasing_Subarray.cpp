class Solution {
public:
    // TC: O(N) SC: O(1)
    int longestMonotonicSubarray(vector<int>& nums) {
        int n= nums.size();
        int ans_inc = 1;
        int ans_dec = 1;
        int res = 1;
        for(int i=1; i<n; i++)
        {
            if (nums[i] <= nums[i-1])
            {
                res = max(res, ans_inc);
                ans_inc = 1;
            }
            else ans_inc ++;

            if(nums[i] >= nums[i-1])
            {
                res = max(res, ans_dec);
                ans_dec = 1;
            }
            else ans_dec ++;
        }
        
        res = max({res, ans_inc, ans_dec});
        return res;
    }
};
