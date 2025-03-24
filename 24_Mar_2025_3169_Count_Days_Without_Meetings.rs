use std::cmp::max;
// TC : O(N) SC: O(1)
impl Solution {
    pub fn count_days(days: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let n = meetings.len();
        let mut meetings = meetings.clone();
        meetings.sort();
        println!("{:?}", meetings);

        let mut ans = days;

        let mut i =0;
        for j in 0..n{
            if meetings[j][0] <= meetings[i][1]{
                meetings[i][1]= max(meetings[i][1], meetings[j][1]);
            }
            else{
                ans -= (meetings[i][1]- meetings[i][0] + 1);
                i=j;
            }
        }

        ans -= (meetings[i][1]- meetings[i][0] + 1);
        // println!("{:?}", meetings);

        return ans;
    }
}
