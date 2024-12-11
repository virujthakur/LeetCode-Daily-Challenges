use std::cmp;
impl Solution {
    //TC: O(N) SC: O(N)
    pub fn maximum_beauty(nums: Vec<i32>, k: i32) -> i32 {
        let mut f: [u32; 300_003] = [0; 300_003];
        for num in nums{
            f[(num - k + 100_000) as usize] +=1;
            f[(num + k + 100_000 + 1) as usize] -=1;
        }
        
        let mut s = 0;
        let mut ans = 0;
        for i in 0..300_003{
            s+= f[i];
            f[i]= s;
            ans = cmp::max(ans, f[i]);
        }
        
        return ans as i32;
    }
}
