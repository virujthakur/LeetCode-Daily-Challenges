impl Solution {
    // TC : O(N) SC; O(1)
    pub fn apply_operations(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = &mut nums.clone();
        let n = nums.len();
        for i in 0..n-1{
            if nums[i] == nums[i+1]{
                nums[i]*=2;
                nums[i+1]=0;
            }
        }

        let mut ans : Vec<i32> = vec![0; n];
        let mut j = 0 as usize;
        for i in 0..n{
            if nums[i] > 0{
                ans[j] = nums[i];
                j+=1;
            }
        }

        return ans;

    }
}
