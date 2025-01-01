use core::cmp::max;
//TC: O(N) SC: O(N)
impl Solution {
    pub fn max_score(s: String) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes(); 

        let mut left_score = vec![0; n];   
        let mut right_score = vec![0; n]; 

        let mut count = 0;
        for i in 0..n {
            if bytes[i] == b'0' { 
                count += 1;
            }
            left_score[i] = count;
        }

        count = 0;
        for i in (0..n).rev() { 
            if bytes[i] == b'1' { 
                count += 1;
            }
            right_score[i] = count;
        }

        let mut ans = 0;
        
        for i in 0..n - 1 { 
            ans = max(ans, left_score[i] + right_score[i + 1]);
        }

        ans
    }
}
