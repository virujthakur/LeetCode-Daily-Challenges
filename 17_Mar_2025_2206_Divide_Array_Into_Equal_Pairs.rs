use std::collections::HashMap;
impl Solution {
    // TC: O(N) SC: O(N)
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut f : HashMap<i32, i32> = HashMap::new();
        let n = nums.len();
        for i in 0..n{
            *f.entry(nums[i]).or_insert(0)+=1;
        }
        for (k,v) in f.iter(){
            if v %2 == 1{
                return false;
            }
        }
        return true;
    }
}
