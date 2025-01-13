use std::collections::HashMap;
impl Solution {
    //TC: O(N) SC: O(26)
    pub fn minimum_length(s: String) -> i32 {
        let mut f = HashMap::new();
        for c in s.chars(){
            *f.entry(c).or_insert(0)+=1;
        }

        println!("{:?}", f);
        let mut ans = 0;
        for (k,v) in f.iter(){
            if *v > 2{
                if v%2 == 0{
                    ans+=2;
                }
                else{
                    ans+=1;
                }
            }
            else{
                ans+= v;
            }
        }

        return ans;
        
    }
}
