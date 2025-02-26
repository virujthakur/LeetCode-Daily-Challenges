use std::cmp::max;
use std::cmp::min;

impl Solution {
    // TC: O(N) SC: O(1)
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let n= nums.len();

        let mut ans = 0;
        let mut max_subarray_sum = -100_000_000;

        for i in 0..n{
            if ans < 0{
                ans = 0;
            }
            ans += nums[i];
            max_subarray_sum = max(ans, max_subarray_sum);
        }

        let mut min_subarray_sum = 100_000_000;
        ans = 0;

        for i in 0..n{
            if ans > 0{
                ans = 0;
            }
            ans += nums[i];
            min_subarray_sum = min(ans, min_subarray_sum);
        }

        return max(max_subarray_sum.abs(), min_subarray_sum.abs());


    }
}
