use std::cmp::max;
impl Solution {
    // TC: O(N^3) SC: O(1)
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n{
            for j in i+1..n{
                for k in j+1..n{
                    ans = max(ans, (nums[i] as i64- nums[j] as i64)* nums[k] as i64);
                }
            }
        }
        return ans;
    }
}
