use std::collections::HashMap;
// TC: O(N*N) SC: O(N*N*N)
impl Solution {
    pub fn isSpecial(s: &str, f: &HashMap<char, u32>) -> bool{
        if f.len() ==1{
            return true;
        }
        else{
            return false;
        }
    }
    
    pub fn maximum_length(s: String) -> i32 {
        
        let mut f2 : HashMap<String, u32> = HashMap:: new();
        
        let chars: Vec<char> = s.chars().collect();
        
        for i in 0..chars.len(){
            let mut cur = String::from("");
            let mut f1 : HashMap<char, u32> = HashMap:: new();
            
            for j in i..chars.len(){
                cur.push(chars[j]);
                *f1.entry(chars[j]).or_insert(0) += 1;

                if Solution::isSpecial(&cur, &f1) { // Corrected the call to `is_special` using `Solution::`.
                    *f2.entry(cur.clone()).or_insert(0) += 1; // Use `entry` to update the frequency map.
                }
            }
        }
        
        let mut ans = String::from("");
        for (k,v) in f2{
            if v>=3{
                if k.len() > ans.len(){
                    ans= k;
                }
            }
        }
        
        if ans.len()> 0{
            ans.len() as i32
        }
        else {
            -1
        }
        
    }
}
