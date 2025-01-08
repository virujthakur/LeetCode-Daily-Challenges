impl Solution {
    //TC: O(N^3) SC: O(1)
    pub fn is_prefix_and_suffix(word1: &str, word2: &str) -> bool {
        let prefix_match = word2.starts_with(word1);
        let suffix_match = word2.ends_with(word1);
        prefix_match && suffix_match
    }
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut ans = 0;
        for i in 0..n{
            for j in i+1..n{
                if Self::is_prefix_and_suffix(&words[i], &words[j]){
                    ans+=1;
                }
            }
        }

        return ans;
    }
}
