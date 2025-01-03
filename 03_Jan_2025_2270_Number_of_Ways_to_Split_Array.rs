impl Solution {
    //TC: O(N) SC: O(N)
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut suffix : Vec<i64> = vec![0; n];

        let mut s : i64 = 0;
        for i in (0..n).rev(){
            s+= nums[i] as i64;
            suffix[i] = s;
        }

        s = 0;
        let mut ans = 0;
        for i in 0..n-1{
            s += nums[i] as i64;
            if s >= suffix[i+1]{
                ans +=1;
            }
        }

        ans
        
    }
}
