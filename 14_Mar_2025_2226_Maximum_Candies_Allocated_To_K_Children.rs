use std::cmp::max;
impl Solution {
    // TC: O(NLOGN) SC: O(1)
    pub fn isValid(candies: &Vec<i32>, mid: i64, k: i64) -> bool
    {
        let n= candies.len();
        let mut sum = 0i64;
        for i in 0..n{
            sum += candies[i] as i64 / mid;
        }

        return sum >=k;
        
    }
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        let mut lo = 1i32;
        let mut hi = 1_000_000_0i32;
        let mut ans = 0;

        while lo <= hi{
            let mid = lo + (hi-lo)/2;
            if Self::isValid(&candies, mid as i64, k){
                ans = max(ans, mid);
                lo= mid+1;
            }
            else{
                hi = mid-1;
            }
        }

        return ans;
    }
}
