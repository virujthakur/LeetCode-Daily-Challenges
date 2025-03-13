use std::cmp::min;
impl Solution {
    // TC: O(NLOGN) SC: O(N)
    pub fn isValid(nums: &Vec<i32>, queries: &Vec<Vec<i32>>, k: usize) -> bool
    {
        let n = nums.len();
        let mut prefix = vec![0; (n+1)];

        for (i,q) in queries.into_iter().enumerate(){
            if i == k{
                break;
            }
            prefix[q[0] as usize] -= q[2];
            prefix[q[1] as usize +1] += q[2];
        }

        // println!("{:?}", prefix);
        let mut s = 0;
        for i in 0..n{
            s += prefix[i];
            prefix[i] = s + nums[i];

            if prefix[i] > 0{
                return false;
            }
        }

        return true;


    }
    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = queries.len();
        let mut l =0;
        let mut h = n+1;
        let mut ans = n+1;

        while l<h{
            let mid = l + (h-l)/2;
            // println!("{}", mid);
            if Self::isValid(&nums, &queries, mid){
                ans = min(ans, mid);
                h = mid;
            }
            else{
                l = mid+1;
            }
        }

        if ans as usize == (n+1){
            return -1;
        }

        (ans) as i32
        
    }
}
