use std::collections::HashMap;
impl Solution {
    //TC : O(N) SC: O(26)
    pub fn can_construct(s: String, k: i32) -> bool {
        let n= s.len();
        if k == n as i32{
            return true;
        }

        if k > n as i32{
            return false;
        }

        let mut f = HashMap::new();
        for c in s.chars(){
            *f.entry(c).or_insert(0)+=1;
        }

        let mut cnt_odd = 0;
        for (k,v) in f.iter(){
            if v%2 ==1{
                cnt_odd +=1;
            }
        }

        if cnt_odd > k{
            return false;
        }

        return true;
    }
}
