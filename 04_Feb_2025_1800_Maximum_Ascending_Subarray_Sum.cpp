class Solution {
public:
    // TC : O(N) SC: O(1)
    int maxAscendingSum(vector<int>& nums) {
       int n = nums.size();
       int res = 0;
       int ans = nums[0];
       for(int i=1; i<n; i++)
       {
            if (nums[i] <= nums[i-1])
            {
                res = max(ans, res);
                ans = nums[i];
            }
            else{
                ans+= nums[i];
            }
       } 

       res = max(ans, res);
       return res;
    }
};
