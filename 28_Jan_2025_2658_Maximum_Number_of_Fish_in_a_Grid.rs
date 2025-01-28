impl Solution {
    // TC: O(M*N*M*N) SC: O(M*N)
    pub fn dfs(grid: & mut Vec<Vec<i32>>, directions : & Vec<(i32,i32)>, i: i32, j: i32) -> i32
    {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;

        if i>= m || j>= n || i < 0 || j< 0 || grid[i as usize][j as usize] <=0{
            return 0;
        }
        
        let mut ans = grid[i as usize][j as usize];
        grid[i as usize][j as usize] = -1;

        for d in directions{
            let newi = i+ d.0;
            let newj = j+ d.1;
            ans += Self::dfs(grid, directions, newi, newj);
        }

        return ans;
    }
    pub fn find_max_fish(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;
        let directions : Vec<(i32, i32)> = vec![(0,1), (1,0), (0,-1), (-1,0)];

        for i in 0..m{
            for j in 0..n{
                // println!("{}, {}", i,j);
                let mut newgrid= grid.clone();
                res = std::cmp::max(Self::dfs(& mut newgrid, & directions,i as i32,j as i32), res);
            }
        }

        return res;
    }
}
