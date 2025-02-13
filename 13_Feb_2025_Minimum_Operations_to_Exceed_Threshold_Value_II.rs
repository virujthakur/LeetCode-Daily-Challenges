use std::collections::BinaryHeap;
use std::cmp::min;
use std::cmp::max;
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut pq : BinaryHeap<i64> = BinaryHeap::new();
        for num in nums{
            pq.push((-num) as i64);
        }

        let mut ops = 0;
        while let Some(top) = pq.pop(){
            if pq.len() < 1{
                break;
            }

            if -top >= k as i64{
                break;
            }

            let top2 = pq.pop().unwrap();
            pq.push(-(min(-top, -top2)* 2 + max(-top, -top2)));
            // println!("{:?}, {}, {}", pq, top, top2);
            ops+=1;
        }

        return ops;

    }
}
