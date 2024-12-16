use std::collections::BinaryHeap;
impl Solution {
    // TC: O(K LOG N) SC: O(N)
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        let n = nums.len();
        let mut heap = BinaryHeap :: new();
        let mut ans = nums.clone();
        let mut k = k;
        for i in 0..n{
            heap.push((-nums[i], -(i as i32)));
        }
        
        while k>0{
            let x = heap.pop();
            // println!("min value = {}, {}", x.unwrap().0, x.unwrap().1);
            ans[-(x.unwrap().1) as usize] *= multiplier;
            heap.push((-ans[-(x.unwrap().1) as usize], x.unwrap().1));
            k-=1;
        }
        
        return ans;
    }
}
