use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    //TC: O(NLOGN) SC: O(N)
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        let mut f= HashMap::new();
        for num in nums{
            let mut temp = num;
            let mut digit_sum = 0;
            while temp > 0{
                digit_sum+= temp%10;
                temp/=10;
            }
            // println!("{}, {}", digit_sum, num);
            f.entry(digit_sum).or_insert(Vec::new()).push(num);
        }

        let mut ans = -1;
        // println!("{:?}", f);
        for (k,mut v) in f.into_iter(){
            if v.len()>= 2{
                v.sort();
                ans = max(ans, v[v.len()-1]+ v[v.len()-2]);
            }
        }

        return ans;
    }
}
