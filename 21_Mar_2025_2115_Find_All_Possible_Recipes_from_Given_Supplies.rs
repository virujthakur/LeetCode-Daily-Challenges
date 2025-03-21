use std::collections::HashSet;
use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    // TC: O(N) SC: O(N)
    pub fn find_all_recipes(recipes: Vec<String>, ingredients: Vec<Vec<String>>, supplies: Vec<String>) -> Vec<String> {
        let n = recipes.len();
        let mut graph = vec![vec![]; n];
        let mut indegree = vec![0; n];
        
        let mut index_of_recipe = HashMap::new();
        for i in 0..n{
            index_of_recipe.insert(recipes[i].clone(), i);
        }

        for i in 0..n{
            let m = ingredients[i].len();
            for j in 0..m{
                if index_of_recipe.contains_key(&ingredients[i][j]){
                    graph[index_of_recipe[&ingredients[i][j]]].push(i);
                    indegree[i]+=1;
                }
            }
        }

        // println!("{:?}, {:?}", graph, indegree);

        let mut supplies_set = HashSet::new();
        let k = supplies.len();
        for i in 0..k{
            supplies_set.insert(supplies[i].clone());
        }

        let mut q = VecDeque::new();
        for i in 0..n{
            if indegree[i] == 0{
                q.push_back(i);
            }
        }

        let mut ans = Vec::new();

        while let Some(top) = q.pop_front(){
            let m = ingredients[top].len();
            let mut can_make = true;
            for j in 0..m{
                if !supplies_set.contains(&ingredients[top][j]){
                    // println!("{:?}, {:?}", recipes[top], ingredients[top][j]);
                    can_make = false;
                    break;
                }
            }

            if can_make{
                ans.push(recipes[top].clone());
                supplies_set.insert(recipes[top].clone());
            }

            // println!("{:?}", supplies_set);
            
            for nbr in graph[top].clone(){
                indegree[nbr]-=1;
                if indegree[nbr] == 0{
                    q.push_back(nbr);
                }
            }
        }

        return ans;
    }
}
