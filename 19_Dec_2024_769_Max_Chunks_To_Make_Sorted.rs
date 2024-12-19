impl Solution {
    // TC: O(N) SC: O(1)
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut ans = 0;
        let n = arr.len();
        let mut mx = -1;
        
        for i in 0..n{
            mx = std::cmp::max(arr[i], mx);
            if mx == i as i32{
                ans+=1;
            }
        }
        
        return ans;
        
    }
}
