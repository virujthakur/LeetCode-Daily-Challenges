use std::collections::BinaryHeap;
impl Solution {
    //TC: O(M*N*LOG(M*N)) SC: O(M*N)
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        let m = height_map.len();
        if m == 0 {
            return 0;
        }
        let n = height_map[0].len();
        if n == 0 {
            return 0;
        }

        let mut visited = vec![vec![false; n]; m];
        let mut pq = BinaryHeap::new();

        // Add boundary cells to the priority queue
        for i in 0..m {
            for j in 0..n {
                if i == 0 || j == 0 || i == m - 1 || j == n - 1 {
                    visited[i][j] = true;
                    pq.push((-height_map[i][j], i, j)); // Use negative height to simulate min-heap
                }
            }
        }

        let directions = vec![(0, 1), (-1, 0), (1, 0), (0, -1)];
        let mut ans = 0;

        while let Some((neg_cur_height, r, c)) = pq.pop() {
            let cur_height = -neg_cur_height;

            for (dx, dy) in &directions {
                let rdash = r as isize + dx;
                let cdash = c as isize + dy;

                if rdash >= 0
                    && rdash < m as isize
                    && cdash >= 0
                    && cdash < n as isize
                    && !visited[rdash as usize][cdash as usize]
                {
                    let rdash = rdash as usize;
                    let cdash = cdash as usize;
                    let new_height = height_map[rdash][cdash];

                    if new_height < cur_height {
                        ans += cur_height - new_height;
                        pq.push((-cur_height, rdash, cdash));
                    } else {
                        pq.push((-new_height, rdash, cdash));
                    }

                    visited[rdash][cdash] = true;
                }
            }
        }

        ans
    }
}
