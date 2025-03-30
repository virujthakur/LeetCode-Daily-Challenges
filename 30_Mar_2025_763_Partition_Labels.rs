use std::cmp::max;
use std::collections::HashMap;
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut st =-1;
        let mut en =0i32;

        let n = s.len();
        let mut s : Vec<char> = s.chars().collect();

        let mut last_occ : HashMap<char, usize> = HashMap::new();
        for (i,c) in s.iter().enumerate(){
            last_occ.insert(*c,i);
        }

        let mut ans = Vec::new();
        let mut max_last_occ = 0;
        while en < n as i32{
            max_last_occ = max(max_last_occ, last_occ[&s[en as usize]] as i32);

            if max_last_occ == en{
                ans.push((en-st));
                st = en;
            }
            // println!("{}, {}, {}", st, en, max_last_occ);
            en+=1;
        }

        return ans;
        
    }
}
