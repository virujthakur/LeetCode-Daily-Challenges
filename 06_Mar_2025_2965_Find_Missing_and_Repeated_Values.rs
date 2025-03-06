impl Solution {
    // TC: O(N^2) SC: O(N^2)
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len();
        let mut f = vec![0; n*n+1];
        let mut ans : Vec<i32> = vec![-1; 2];
        for i in 0..n{
            for j in 0..n{
                f[grid[i][j] as usize]+=1;
            }
        }

        for i in 1..n*n+1{
            if f[i] == 0{
                ans[1] = i as i32;
            }
            if f[i] == 2{
                ans[0] = i as i32;
            }
        }

        return ans;
    }
}
