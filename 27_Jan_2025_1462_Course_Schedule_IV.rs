use std::collections::VecDeque;
impl Solution {
    //TC: O(N^2) SC: O(N^2)
    pub fn check_if_prerequisite(num_courses: i32, prerequisites: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut q : VecDeque<usize> = VecDeque::new();
        let mut graph = vec![vec![]; num_courses as usize];

        for p in &prerequisites{
            graph[p[0] as usize].push(p[1] as usize);
        }

        let mut all_prequisites = vec![vec![false; num_courses as usize]; num_courses as usize];

        for i in 0.. num_courses{
            let mut q = VecDeque::new();
            q.push_back(i as usize);
            let mut visited = vec![false; num_courses as usize];

            while let Some(top) = q.pop_front(){
                visited[top]= true;
                for nbr in &graph[top]{
                    if !visited[*nbr]{
                        q.push_back(*nbr);
                        all_prequisites[i as usize][*nbr] = true;
                    }
                }
            }
        }
        

        let mut res = Vec::new();
        for q in &queries{
            res.push(all_prequisites[q[0] as usize][q[1] as usize]);
        }

        return res;
    }
}
