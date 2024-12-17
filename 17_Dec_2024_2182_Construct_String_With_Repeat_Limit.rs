impl Solution {
    // TC: O(26*26*N) SC: O(1)
    pub fn repeat_limited_string(s: String, repeat_limit: i32) -> String {
        let mut f = [0; 26];
        
        for c in s.chars(){
            f[(c as u8 - ('a' as u8)) as usize] +=1;
        }
        
        let mut ans = String::from("");
        let mut i : i32 = 25;
        let mut prev_j = -1;
        
        while i >= 0{
            if f[i as usize] == 0{
                i-=1;
                continue;
            }
            
            let mut new_repeat_limit = repeat_limit;
            if i== prev_j{
                new_repeat_limit -=1;
            }
            
            let mut char_s = ((i as u8 + ('a' as u8)) as char).to_string();
            let mut char_string = char_s.repeat(std::cmp::min(f[i as usize], new_repeat_limit as usize));
            f[i as usize] -= std::cmp::min(f[i as usize], new_repeat_limit as usize);
            
            
            let mut j = i.clone();
            j-=1;
            // println!("{}, {}", i, j);
            while (j >=0 && f[j as usize] == 0){
                j-=1;
            }
            
            // println!("{}", j);
            
            if j==-1{
                ans+= &char_string;
                return ans;
            }
            else{
                let mut char2_s = ((j as u8 + ('a' as u8)) as char).to_string();
                char_string += &char2_s;
                f[j as usize]-= 1;
            }
            
            if f[i as usize] == 0{
                i-=1;
            }
            ans+= &char_string;
            prev_j = j;
        }
        
        return ans;
        
    }
}
