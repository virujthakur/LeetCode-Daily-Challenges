use std::collections::BinaryHeap;
// TC: O(M*N (LOG(M*N))) SC: O(M*N)
impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let n = queries.len();
        let mut ans = vec![0; n];
        let mut new_queries = Vec::new();
        for (i,query) in queries.iter().enumerate(){
            new_queries.push((*query, i));
        }
    
        new_queries.sort();

        let mut q = BinaryHeap::new();
        q.push((-grid[0][0], 0, 0));
        let dir : Vec<(i32, i32)> = vec![(0,1), (1,0), (0,-1), (-1,0)];
        let mut visited = vec![vec![false; grid[0].len()]; grid.len()];

        let mut q_ptr = 0;

        while let Some(top)= q.pop(){

            while q_ptr < n && grid[top.1][top.2] >= new_queries[q_ptr].0{
                q_ptr +=1;
            }

            if q_ptr == n{
                break;
            }

            // println!("{:?}, {}", top, q_ptr);

            if visited[top.1][top.2]== true{
                continue;
            }

            
            visited[top.1][top.2]= true;
            ans[q_ptr]+=1;

            for d in dir.clone(){
                let newx = (top.1 as i32 + d.0) ;
                let newy = (top.2 as i32 + d.1);
                if newx >=0i32 && newy >=0i32 && newx < grid.len() as i32 && newy < grid[0].len() as i32 && visited[newx as usize][newy as usize] == false{
                    q.push((-grid[newx as usize][newy as usize], newx as usize, newy as usize));
                }
            }
        }

        // println!("{:?}", ans);

        for i in 1..n{
            ans[i] += ans[i-1];
        }

        // println!("{:?}", ans);

        let mut res= vec![0; n];
        for i in 0..n{
            res[new_queries[i].1] = ans[i];
        }

        return res;
    }
}
