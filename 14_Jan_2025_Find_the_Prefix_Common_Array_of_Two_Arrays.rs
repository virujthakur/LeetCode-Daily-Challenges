use std::collections::HashSet;
impl Solution {
    //TC: O(N^2) SC: O(N)
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut f1 = HashSet::new();
        let mut f2 = HashSet::new();
        let mut ans = Vec::new();
        let n = a.len();
        for i in 0..n{
            f1.insert(a[i]);
            f2.insert(b[i]);

            let mut res = 0;
            for j in 1..=50{
                if f1.contains(&j) && f2.contains(&j){
                    res+=1;
                }
            }

            ans.push(res);
        }

        return ans;
    }
}
