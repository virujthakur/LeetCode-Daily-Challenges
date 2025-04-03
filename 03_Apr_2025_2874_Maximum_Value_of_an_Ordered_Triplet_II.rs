use std::cmp::max;
impl Solution {
    // TC: O(N) SC: O(N)
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut prefix_max = vec![0i64; n];
        let mut suffix_max = vec![0i64; n];

        for i in 1..n{
            prefix_max[i] = max(nums[i-1] as i64, prefix_max[i-1]);
            suffix_max[n-1-i] = max(nums[n-i] as i64, suffix_max[n-i]);
        }

        // println!("{:?}", prefix_max);
        // println!("{:?}", suffix_max);

        let mut ans = 0;
        for j in 0..n{
            ans= max(ans, (prefix_max[j]- nums[j] as i64) * suffix_max[j]);
        }

        return ans;
    }
}
