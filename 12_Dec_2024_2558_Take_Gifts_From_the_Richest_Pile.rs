use std::collections::BinaryHeap;
impl Solution {
    pub fn pick_gifts(mut gifts: Vec<i32>, mut k: i32) -> i64 {
        let mut maxHeap = BinaryHeap::new();
        let n = gifts.len();
        for i in 0..n{
            maxHeap.push((gifts[i] as i64, i));
        }
        
        while k>0 {
            let top = maxHeap.pop().unwrap();
            let sqr : i64 = f64::sqrt(top.0 as f64) as i64;
            gifts[top.1 as usize] = sqr as i32;
            maxHeap.push((sqr, top.1));
            k-=1;
        }
        
        // println!("{:?}", gifts);
        
        let mut ans : i64 = 0;
        for i in 0..n{
            ans += gifts[i] as i64;
        }
        
        return ans;
    }
}
