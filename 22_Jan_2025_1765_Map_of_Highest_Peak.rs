use std::collections::VecDeque;
impl Solution {
    //TC: O(M*N) SC: O(M*N)
    pub fn highest_peak(mut is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut q : VecDeque<(i32, i32, i32)> = VecDeque::new();

        let m = is_water.len();
        let n = is_water[0].len();

        for i in 0..m{
            for j in 0..n{
                if is_water[i][j] == 1{
                    q.push_back((0,i as i32,j as i32));
                }
            }
        }

        let mut visited = vec![vec![0;n];m];
        let directions : Vec<(i32, i32)> = vec![(0,1), (1,0), (0,-1), (-1,0)];

        while let Some(top) = q.pop_front(){

            if visited[top.1 as usize][top.2 as usize]== 1{
                continue;
            }

            visited[top.1 as usize][top.2 as usize]= 1;
            is_water[top.1 as usize][top.2 as usize] = top.0;

            for d in &directions{
                let newx = top.1 + d.0;
                let newy = top.2 + d.1;

                if newx >=0 as i32 && newy>=0 as i32 && newx < m as i32 && newy < n as i32 && visited[newx as usize][newy as usize] == 0{
                    q.push_back((top.0+1, newx, newy));
                }
            }

        }

        return is_water;

    }
}
