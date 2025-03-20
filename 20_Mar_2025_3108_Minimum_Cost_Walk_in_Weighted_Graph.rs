use std::collections::HashMap;
impl Solution {
    //TC: O(EDGES) SC: O(N)
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
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let mut parent = vec![0; n as usize];
        let mut rank = vec![1; n as usize];
        for i in 0..n as usize{
            parent[i] = i;
        }

        for e in edges.clone(){
            Self::union(&mut parent, &mut rank, e[0] as usize, e[1] as usize);
        }

        let mut componentAnd : HashMap<usize, usize> = HashMap::new();
        for e in edges.clone(){
            let p = Self::find(&mut parent, e[0] as usize);
            *componentAnd.entry(p).or_insert(e[2] as usize) &= e[2] as usize;
        }

        // println!("{:?}", componentAnd);

        let mut ans = Vec::new();
        for q in query{
            let p1 = Self::find(&mut parent, q[0] as usize);
            let p2 = Self::find(&mut parent, q[1] as usize);

            if p1 != p2{
                ans.push(-1);
            }
            else{
                ans.push(componentAnd[&p1] as i32);
            }
        }

        return ans;
    }
}
