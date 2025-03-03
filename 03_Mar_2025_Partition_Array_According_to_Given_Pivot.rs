impl Solution {
    // TC: O(N) SC: O(N)
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        let n = nums.len();
        for i in 0..n{
            if nums[i] < pivot{
                ans.push(nums[i]);
            }
        }

        for i in 0..n{
            if nums[i] == pivot{
                ans.push(nums[i]);
            }
        }

        for i in 0..n{
            if nums[i] > pivot{
                ans.push(nums[i]);
            }
        }
        return ans;
    }
}
