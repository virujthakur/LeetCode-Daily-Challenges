use std::collections::HashSet;
impl Solution {
    //TC: O(N^2 * M^2) SC: O(1)
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let n = words.len();
        let mut ans= HashSet::new();

        for word1 in &words{
            for word2 in &words{
                if *word1 == *word2{
                    continue;
                }

                if word2.contains(word1){
                    ans.insert(word1.clone());
                }
            }
        }

        // println!("{:?}", ans);
        return ans.into_iter().collect();
    }
}
