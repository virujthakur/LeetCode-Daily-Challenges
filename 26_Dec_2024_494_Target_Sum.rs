impl Solution {
    //TC: O(N*target) SC : O(N* target)
    pub fn recur(idx : usize, nums: &Vec<i32>, target: i32, dp: &mut Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        if idx == n{
            if target == 0{
                return 1;
            }
            else{
                return 0;
            }
        }
        
        if dp[idx][(target + 1000) as usize] != -1{
            return dp[idx][(target + 1000) as usize];
        }
        
        let mut ans = 0;
        ans+= Self::recur(idx+1, nums, target - nums[idx], dp);
        ans+= Self::recur(idx+1, nums, target + nums[idx], dp);
        
        dp[idx][(target+ 1000) as usize]= ans;
        return ans;
    }
    
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let mut dp = vec![vec![-1; 3001]; 21];
        Self::recur(0, &nums, target, &mut dp)
    }
}
