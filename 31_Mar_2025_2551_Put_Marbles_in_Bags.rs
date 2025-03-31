use std::collections::BinaryHeap;
impl Solution {
    // TC: O(NLOGN) SC: O(N)
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let n = weights.len();
        let mut mxHeap = BinaryHeap::new();
        let mut mnHeap = BinaryHeap::new();
        for i in 1..n{
            mxHeap.push(weights[i]+ weights[i-1]);
            mnHeap.push(-(weights[i] + weights[i-1]));
        }

        let mut mxSum = 0i64;
        let mut mnSum = 0i64;
        let mut cnt = 0;

        while cnt < k-1{
            mxSum += mxHeap.pop().unwrap() as i64;
            cnt +=1;
        }

        let mut cnt = 0;
        while cnt < k-1{
            mnSum += mnHeap.pop().unwrap() as i64;
            cnt+=1;
        }

        return mxSum + mnSum;
    }
}
