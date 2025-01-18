use std::collections::BinaryHeap;

// TC: O(M*N* LOG(M*N)) SC: O(M*N)
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let m : i32 = grid.len() as i32;
        let n : i32 = grid[0].len() as i32;

        let directions: [(i32, i32); 4] = [(0,1), (0,-1), (1, 0), (-1, 0)];
        let mut visited = vec![vec![false; n as usize]; m as usize];

        let mut pq = BinaryHeap::new();
        pq.push((0, 0, 0));

        while let Some(top) = pq.pop(){
            let x : i32 = top.1;
            let y : i32 = top.2;
            let cost = -(top.0);

            if visited[x as usize][y as usize] == true{
                continue;
            }

            visited[x as usize][y as usize] = true;

            if x == m-1 && y == n-1{
                return cost;
            }

            for (i,d) in directions.iter().enumerate(){
                let newx = x + d.0;
                let newy = y + d.1;

                if newx >=0 && newx < m && newy >=0 && newy < n && visited[newx as usize][newy as usize] == false{
                    if grid[x as usize][y as usize] == i as i32 +1{
                        pq.push((-(cost), newx, newy));
                    }
                    else{
                        pq.push((-(cost +1), newx, newy));
                    }
                }
            }
        }

        return -1;
    }
}
