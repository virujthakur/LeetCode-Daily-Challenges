use std::collections::BinaryHeap;
impl Solution {
    // TC: O(ELOGV) SC: O(N)
    pub fn count_paths(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let MOD = 1_000_000_007;
        let mut pq = BinaryHeap::new();
        let mut distTo : Vec<i64> = vec![i64::MAX; n as usize];
        let mut graph = vec![vec![]; n as usize];
        for r in roads{
            graph[r[0] as usize].push((r[1] as usize, r[2] as i64));
            graph[r[1] as usize].push((r[0] as usize, r[2] as i64));

        }

        let mut cnt : Vec<i64> = vec![1i64; n as usize];
        distTo[0] = 0;
        pq.push((0, 0));

        while let Some(top) = pq.pop(){
            // println!("{:?}" , top);
            for (nbr, nbr_cost) in graph[top.1].clone(){
                if distTo[nbr] > -(top.0) + nbr_cost{
                    distTo[nbr] = -(top.0) + nbr_cost;
                    pq.push((-distTo[nbr], nbr));
                    cnt[nbr] = cnt[top.1] % MOD;
                }
                else if distTo[nbr] == -(top.0) + nbr_cost{
                    cnt[nbr] = (cnt[top.1] % MOD + cnt[nbr] % MOD) % MOD;
                }
            }
        }

        return cnt[n as usize - 1] as i32;
    }
}
