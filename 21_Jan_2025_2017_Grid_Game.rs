use std::collections::HashMap;
impl Solution {
    //TC: O(N) SC: O(N)
    pub fn grid_game(mut grid: Vec<Vec<i32>>) -> i64 {
        let n = grid[0].len();
        let mut prefix : Vec<Vec<i64>> = vec![vec![0;n];2];
        let mut s1 : i64 = 0;
        let mut s2 : i64 = 0;
        for i in 0..n{
            s1+= grid[0][i] as i64;
            s2+= grid[1][i] as i64;
            prefix[0][i] = s1;
            prefix[1][i] = s2;
        }

        let mut res : i64 = 1000_000_000_000_000_000;
        let mut p1  : i64 = 0;
        for i in 0..n{
            let mut newp1 : i64 = prefix[0][i] + s2;
            // println!("{}", i);
            if i as i64 -1 >=0{
                newp1 -= prefix[1][i-1];
            }
            // println!("{}", newp1);
            
            p1 = std::cmp::max(p1, newp1);
            let mut ans = s1- prefix[0][i];
            if i as i64 -1 >=0{
                ans = std::cmp::max(ans, prefix[1][i-1]);
            }
            
            res = std::cmp::min(ans, res);
            

        }

        return res;
    }
}
