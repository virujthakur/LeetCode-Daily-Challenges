impl Solution {
    pub fn isValid(n_2: &str, n: i32, idx: i32, prev_sum: i32) -> i32
    {
        let m = n_2.len() as i32;

        if n == 0 && idx == m && prev_sum == 0 {
            return 1;
        }

        if n < 0 || idx == m{
            return 0;
        }

        // if dp[idx as usize][prev_sum as usize]!=-1{
        //     return dp[idx as usize][prev_sum as usize];
        // }
        // println!("{}, {}", idx, prev_sum);
        let digit = n_2[idx as usize .. (idx+1) as usize].parse::<i32>().unwrap();
        let ans1 = Self::isValid(n_2, n, idx+1, prev_sum * 10 + digit);
        let ans2 = Self::isValid(n_2, n-(prev_sum* 10 + digit), idx+1, 0);

        // dp[idx as usize][prev_sum as usize]= ans1 | ans2;
        // println!("{}, {}, {}", ans1, ans2, idx);
        return ans1 | ans2;
    }
    
    pub fn punishment_number(n: i32) -> i32 {
        let mut ans = 0;
        for i in 1..=n{
            // let mut dp= vec![vec![-1; 1001]; 7];
            // println!("{:?}", dp);
            if Self::isValid(&(i*i).to_string(), i, 0, 0) == 1{
                // println!("{}, {}", i, i*i);
                ans+= i*i;
            }
        }

        return ans;
    }
}
