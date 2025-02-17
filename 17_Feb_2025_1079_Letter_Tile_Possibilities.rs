use std::collections::HashSet;
impl Solution {
    //TC: (N*N!) SC: O(N * N!)
    pub fn recur(tiles: &str, path: String, visited: &mut Vec<bool> , result: &mut HashSet<String>)
    {
        if path.len() == tiles.len(){
            return;
        }

        for i in 0..tiles.len(){
            if visited[i]== false
            {
                visited[i]= true;
                result.insert(path.clone() + &tiles[i..i+1]);
                Self::recur(tiles, path.clone() + &tiles[i..i+1], visited, result); 
                visited[i]= false;
            }
        }
    }
    pub fn num_tile_possibilities(tiles: String) -> i32 {
        let mut result : HashSet<String> = HashSet::new();
        let mut path = String::new();
        let mut visited = vec![false; tiles.len()];
        Self::recur(tiles.as_str(), path, &mut visited, & mut result);

        // println!("{:?}", result);
        return result.len() as i32;
    }
}
