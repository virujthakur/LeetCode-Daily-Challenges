impl Solution {
    //TC: O(N!*N^2) SC: O(N)
    pub fn recur(idx : usize, path: String, pattern: &String, visited:& mut Vec<bool>, ans: & mut String)
    {
        if path.len() == pattern.len()+1{
            if ans.len() == 0{
                *ans = path;
            }
            else{
                *ans = std::cmp::min(ans.clone(), path);
            }
            return;
        }

        let last_char = path.chars().last().unwrap().to_digit(10).unwrap();

        if pattern[idx..idx+1] == *"I"{
            for i in last_char+1..=9{
                if visited[i as usize]== false
                {
                    visited[i as usize]= true;
                    Self::recur(idx+1, path.clone() + &i.to_string(), pattern, visited, ans);
                    visited[i as usize]= false;
                }
            }
        }
        else{
            for i in (1..last_char).rev(){
                if visited[i as usize]== false
                {
                    visited[i as usize]= true;
                    Self::recur(idx+1, path.clone() + &i.to_string(), pattern,visited, ans);
                    visited[i as usize]= false;
                }
            }
        }

    }
    pub fn smallest_number(pattern: String) -> String {
        let mut ans = String::new();
        let mut path = String::new();
        let mut visited = vec![false;10];
        for i in 1..=9{
            visited[i as usize]= true;
            Self::recur(0, path.clone() + &i.to_string(), &pattern, &mut visited, & mut ans);
            visited[i as usize] = false;
        }

        return ans;
    }
}
