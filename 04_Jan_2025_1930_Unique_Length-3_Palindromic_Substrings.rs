use std::collections::HashSet;
impl Solution {
    //TC: O(26*N) SC: O(26*N)
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let mut n = s.len();
        let mut prefix_char_map = vec![vec![0; n+1]; 26];

        for (i, c) in s.chars().enumerate(){
            for j in 'a'..='z'{
                let char_index = (j as u8 - 'a' as u8) as usize;
                if c == j{
                    prefix_char_map[char_index][i+1]= prefix_char_map[char_index][i] + 1;
                }
                else{
                    prefix_char_map[char_index][i+1]= prefix_char_map[char_index][i];
                }
            }
        }

        let mut suffix_char_map = vec![vec![0; n+1]; 26];

        for (i, c) in s.chars().rev().enumerate(){
            let original_index = n - 1 - i;
            for j in 'a'..='z'{
                let char_index = (j as u8 - 'a' as u8) as usize;
                if c == j{
                    suffix_char_map[char_index][original_index]= suffix_char_map[char_index][original_index+1] + 1;
                }
                else{
                    suffix_char_map[char_index][original_index]= suffix_char_map[char_index][original_index+1];
                }
            }
        }
        
        let mut unique = HashSet::new();

        let mut ans = 0;
        for (i,c) in s.chars().enumerate(){
            if i==0 || i==n-1{
                continue;
            }

            for j in 'a'..='z'{
                let char_index = (j as u8 - 'a' as u8) as usize;
                if prefix_char_map[char_index][i] > 0 && suffix_char_map[char_index][i+1] > 0{
                    // println!("{}, {}", i, j);
                    let res = format!("{}{}{}", j, c, j);
                    unique.insert(res);
                    ans+=1;
                }
            }
        }

        return unique.len() as i32;
    }
}
