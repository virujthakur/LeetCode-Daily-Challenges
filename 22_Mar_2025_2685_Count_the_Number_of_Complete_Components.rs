use std::collections::HashMap;
use std::collections::HashSet;
// TC: O(N*N) SC: O(N*N)
impl Solution {
    pub fn union(parent: &mut Vec<usize>, rank: &mut Vec<usize>, x: usize, y: usize){
        let px = Self::find(parent, x);
        let py = Self::find(parent, y);

        if px !=py{
            if rank[px]< rank[py]{
                parent[px] = py;
            }
            else if rank[px] > rank[py]{
                parent[py] = px;
            }
            else{
                parent[py]= px;
                rank[px]+=1;
            }
        }
    }
    pub fn find(parent: &mut Vec<usize>, x: usize) -> usize{
        if parent[x] == x{
            return x;
        }

        parent[x] = Self::find(parent, parent[x]);
        return parent[x];
    }

    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut parent = vec![0; n as usize];
        let mut rank = vec![1; n as usize];
        for i in 0..n as usize{
            parent[i] = i;
        }

        let mut adj_matrix = vec![vec![-1;n as usize]; n as usize];

        for e in edges.clone(){
            Self::union(&mut parent, &mut rank, e[0] as usize, e[1] as usize);
            adj_matrix[e[0] as usize][e[1] as usize] = 1;
            adj_matrix[e[1] as usize][e[0] as usize] = 1;
        }

        let mut components = HashMap::new();
        for e in edges.clone(){
            let p = Self::find(&mut parent, e[0] as usize);
            components.entry(p).or_insert_with(HashSet::new).insert(e[0] as usize);
            components.entry(p).or_insert_with(HashSet::new).insert(e[1] as usize); 
        }

        // println!("{:?}", components);

        let mut ans =0;
        for (k,v) in components.iter(){
            let m = v.len();
            let v : Vec<&usize> = v.into_iter().collect();
            let mut flag = true;
            for i in 0..m{
                if flag{
                    for j in i+1..m{
                        if adj_matrix[*v[i]][*v[j]] !=1{
                            flag = false;
                            break;
                        }
                    }
                }
                else{
                    break;
                }
            }

            if flag{
                ans+=1;
            }
        }

        for i in 0..n as usize{
            if parent[i] == i && rank[i] == 1{
                ans+=1;
            }
        }

        return ans;
    }
}
