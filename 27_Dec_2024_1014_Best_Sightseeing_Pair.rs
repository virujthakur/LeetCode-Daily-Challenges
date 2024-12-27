impl Solution {
    //TC: O(N) SC: O(1)
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let mut myValues1 = values.clone();
        let mut myValues2 = myValues1.clone();
        let n = values.len();
        
        for i in 0..n{
            myValues1[i] += i as i32;
            myValues2[i] -= i as i32;
        }
        
        let mut ans = -1000000000;
        let mut mx = -1000000000;
        for i in (0..n).rev(){
            if i == n-1{
                mx = std::cmp::max(mx, myValues2[i]);
                continue;
            }
            
            ans= std::cmp::max(myValues1[i] + mx, ans);
            mx = std::cmp::max(mx, myValues2[i]);
        }
        
        ans
    }
}
