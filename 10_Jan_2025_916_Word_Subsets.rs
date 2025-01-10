use std::collections::HashMap;
use std::cmp::max;
//TC: O(N*M M=10) SC: O(26)
impl Solution {
    pub fn is_subset(f1: &HashMap<char, i32>, f2 : &HashMap<char, i32>)-> bool{

        for (k,v) in f2.iter(){
            if let Some(value) = f1.get(k){
                if value >= v{
                    continue;
                }
                return false;
            }
            return false;
        }

        return true;
    }
    pub fn word_subsets(words1: Vec<String>, words2: Vec<String>) -> Vec<String> {
        
        let mut ans = Vec::new();
        let mut f3 = HashMap::new();
        
        for word2 in &words2{
            let mut f2 = HashMap::new();
            for c in word2.chars(){
                // println!("{},{}" , word2, c);
                *f2.entry(c).or_insert(0) +=1;
                if let Some(value) = f3.get(&c){
                    f3.insert(c, max(f2[&c], f3[&c]));
                }
                else{
                    f3.insert(c, f2[&c]);
                }
            }
        }

        for word1 in &words1{
            let mut f1 = HashMap::new();
            
            for c in word1.chars(){
                *f1.entry(c).or_insert(0) +=1;
            }
            
            if Self::is_subset(&f1, &f3){
                ans.push(word1.clone());
            }
        }

        return ans;
        
    }
}
