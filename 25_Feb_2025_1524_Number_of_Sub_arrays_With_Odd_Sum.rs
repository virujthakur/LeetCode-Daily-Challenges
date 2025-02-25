use std::collections::HashMap;
impl Solution {
    //TC: O(N) SC: O(1)
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let n = arr.len();

        let mut odd_sums : i64 = 0;
        let mut even_sums : i64 = 0;
        let mut result : i64 = 0;

        for (i, num) in arr.iter().enumerate(){
            if num%2 == 1{
                core::mem::swap(&mut even_sums, &mut odd_sums);
                odd_sums +=1;
            }
            else{
                even_sums+=1;
            }
            
            result = (result+ odd_sums) % 1000_000_007;
        }

        return result as i32;

    }
}
