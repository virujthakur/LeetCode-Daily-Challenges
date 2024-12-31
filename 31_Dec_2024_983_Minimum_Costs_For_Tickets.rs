use std::collections::{HashSet, HashMap};
use std::cmp::min;

//TC: O(365) SC: O(365)
impl Solution {
    pub fn recur(
        day: i32, 
        days: &HashSet<i32>, 
        costs: &Vec<i32>, 
        max_day: i32, 
        memo: &mut HashMap<i32, i32>
    ) -> i32 {
        if day > max_day {
            return 0;
        }

        if let Some(&cached) = memo.get(&day) {
            return cached;
        }

        let mut ans = 1_000_000_000; // Use a large number as an initial value.

        if days.contains(&day) {
            ans = min(ans, costs[0] + Self::recur(day + 1, days, costs, max_day, memo));
            ans = min(ans, costs[1] + Self::recur(day + 7, days, costs, max_day, memo));
            ans = min(ans, costs[2] + Self::recur(day + 30, days, costs, max_day, memo));
        } else {
            ans = Self::recur(day + 1, days, costs, max_day, memo);
        }

        memo.insert(day, ans);
        ans
    }

    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        let max_day = *days.last().unwrap();
        let days: HashSet<i32> = days.into_iter().collect();
        let mut memo = HashMap::new();
        Self::recur(1, &days, &costs, max_day, &mut memo)
    }
}
