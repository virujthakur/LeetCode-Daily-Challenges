impl Solution {
    // TC: O(2^N * N) SC: O(1)
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..(1<<n){
            let mut xor_subset = 0;
            for j in 0..12{
                if (1<<j) & i != 0{
                    xor_subset ^= nums[j];
                }
            }
            ans += xor_subset;
        }
        return ans;
    }
}
