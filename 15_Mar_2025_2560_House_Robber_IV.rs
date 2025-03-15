use std::cmp::min;
impl Solution {
    // TC: O(NLOGN) SC: O(1)
    pub fn isValid(nums: &Vec<i32>, k: i32, mid: i32)-> bool{
        let n = nums.len();
        let mut cnt = 0;
        // cnt of non-ajacent integers less than mid should be >= k
        let mut prev = -2;
        for i in 0..n{
            if i as i32 - 1 == prev{
                continue;
            }

            if nums[i] <= mid{
                cnt+=1;
                prev = i as i32;
            }
        }

        return cnt >= k;
    }

    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let mut lo: i32 = 0;
        let mut hi: i32 = 1_000_000_000;
        let mut ans = 1_000_000_000;

        while lo <= hi{
            let mid = lo + (hi-lo) /2;
            if Self::isValid(&nums, k, mid){
                ans = min(ans, mid);
                hi= mid-1;
            }
            else{
                lo= mid+1;
            }
        }

        return ans;
    }
}
