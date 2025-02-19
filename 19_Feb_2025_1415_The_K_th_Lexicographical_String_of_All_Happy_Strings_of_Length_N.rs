impl Solution {
    //TC : O(3*2^(N-1)) SC: O(3*2^(N-1))
    pub fn generate_happy_strings(idx: usize, prev_char: char, n: usize, path: String, result: &mut Vec<String>)
    {
        if idx == n{
            result.push(path);
            return;
        }

        for i in 'a'..='c'{
            if i != prev_char{
               Self::generate_happy_strings(idx+1, i, n, path.clone() + &i.to_string(), result);
            }
        }
    }

    pub fn get_happy_string(n: i32, k: i32) -> String {
        let mut path = String::new();
        let mut result = Vec::new();
        Self::generate_happy_strings(0, 'z', n as usize, path.clone(), & mut result);

        // println!("{:?}", result);
        if k as usize > result.len(){
            return "".to_string();
        } 
        return result[k as usize -1].clone();
    }
}
