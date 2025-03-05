impl Solution {
    // TC: O(N) SC: O(N)
    pub fn colored_cells(n: i32) -> i64 {
        let mut ans : Vec<i64> = vec![0; (n+1) as usize];
        ans[1] = 1;
        if n >= 2 {
            ans[2] = 5;
        }
        
        for i in 3..(n+1){
            ans[i as usize] = ans[(i-1) as usize] + (i-1) as i64 * 4;
        }

        return ans[n as usize];
    }
}
