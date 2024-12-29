use std::collections::HashMap;
impl Solution {

    const MOD: i64 = 1_000_000_007;

    pub fn recur(
        t_idx: usize,
        w_idx: i32,
        target: &String,
        char_map: &Vec<HashMap<char, i32>>,
        memo: &mut Vec<Vec<Option<i32>>>,
    ) -> i64 {
        if t_idx == target.len() {
            return 1;
        }

        if w_idx == char_map.len() as i32{
            return 0;
        }

        if let Some(cached) = memo[t_idx][(w_idx + 1) as usize] {
            return cached as i64;
        }

        let target_char = target.chars().nth(t_idx).unwrap();

        let mut ans = 0;

        if let Some(&freq) = char_map[w_idx as usize].get(&target_char) {
            ans = (ans
                + (freq as i64
                    * Self::recur(t_idx + 1, w_idx+1, target, char_map, memo) % Self::MOD)
                    % Self::MOD) % Self::MOD;
        }

        ans = (ans + Self::recur(t_idx, w_idx+1, target, char_map, memo)) % Self::MOD ;

        memo[t_idx][(w_idx + 1) as usize] = Some(ans as i32);
        ans
    }

    pub fn num_ways(words: Vec<String>, target: String) -> i32 {
        let word_len = words[0].len();

        // Reverse mapping: char_map[idx] -> HashMap<char, frequency>
        let mut char_map = vec![HashMap::new(); word_len];

        for word in &words {
            for (i, c) in word.chars().enumerate() {
                *char_map[i].entry(c).or_insert(0) += 1;
            }
        }

        // Initialize memoization table: memo[t_idx][w_idx + 1]
        let mut memo = vec![vec![None; word_len + 1]; target.len()];

        Self::recur(0, 0, &target, &char_map, &mut memo) as i32
    }

}
