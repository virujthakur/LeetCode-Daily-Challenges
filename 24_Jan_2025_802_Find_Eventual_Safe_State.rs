use std::collections::HashSet;
//TC: O(N) SC: O(N)

impl Solution {
    fn dfs(
        graph: &Vec<Vec<i32>>,
        src: usize,
        visited: &mut Vec<bool>,
        dfs_visited: &mut Vec<bool>,
        path: &mut HashSet<usize>,
        is_safe: &mut Vec<bool>,
    ) {
        visited[src] = true;
        dfs_visited[src] = true;
        path.insert(src);

        for &neighbor in &graph[src] {
            if !is_safe[neighbor as usize] {
                for &node in path.iter() {
                    is_safe[node as usize] = false;
                }
            } else if visited[neighbor as usize] && dfs_visited[neighbor as usize] {
                for &node in path.iter() {
                    is_safe[node as usize] = false;
                }
            } else if !visited[neighbor as usize] {
                Self::dfs(graph, neighbor as usize, visited, dfs_visited, path, is_safe);
            }
        }

        path.remove(&src);
        dfs_visited[src] = false;
    }

    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();

        let mut is_safe = vec![true; n];
        let mut visited = vec![false; n];
        let mut dfs_visited = vec![false; n];
        let mut path = HashSet::new();

        for i in 0..n {
            if !visited[i] {
                Self::dfs(&graph, i, &mut visited, &mut dfs_visited, &mut path, &mut is_safe);
            }
        }

        let mut answer = Vec::new();
        for i in 0..n {
            if is_safe[i] {
                answer.push(i as i32);
            }
        }

        answer
    }
}
