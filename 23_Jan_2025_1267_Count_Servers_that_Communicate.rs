impl Solution {
    //TC: O(M*N *(M+N)) SC: O(1)
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;

        for i in 0..m{
            for j in 0..n{
                if grid[i][j] == 0{
                    continue;
                }

                let mut flag = false;
                for k in 0..m{
                    if k == i{
                        continue;
                    }

                    if grid[k][j] == 1{
                        flag= true;
                        break;
                    }
                }
                if flag == true{
                    ans+=1;
                    continue;
                }

                for k in 0..n{
                    if j==k{
                        continue;
                    }
                    if grid[i][k] == 1{
                        flag = true;
                        break;
                    }
                }

                if flag == true{
                    ans+=1;
                }
            }
        }

        return ans;
        
    }
}
