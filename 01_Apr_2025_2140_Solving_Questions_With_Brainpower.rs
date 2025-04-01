use std::cmp::max;
impl Solution {
    // TC : O(N) SC: O(N)
    pub fn recur(questions: &Vec<Vec<i32>>, idx: usize, dp: & mut Vec<i64>) ->i64{
        let n = questions.len();
        if idx >= n{
            return 0;
        }

        if dp[idx]!=-1{
            return dp[idx];
        }

        dp[idx] = max(questions[idx][0] as i64+ Self::recur(questions, idx+ questions[idx][1] as usize + 1, dp), Self::recur(questions, idx+1, dp));

        return dp[idx];
    }
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let n= questions.len();
        let mut dp = vec![-1i64; n];

        return Self::recur(&questions, 0, & mut dp);
    }
}
