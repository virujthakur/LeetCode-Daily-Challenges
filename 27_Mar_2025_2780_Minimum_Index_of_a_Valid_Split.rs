use std::collections::HashMap;
impl Solution {
    // TC: O(N) SC: O(N)
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut suffix = vec![0;n];
        let mut f : HashMap<&i32, usize> = HashMap::new();
        for i in (0..n).rev(){
            *f.entry(&nums[i]).or_insert(0) +=1 ;
            if f[&nums[i]] > (n-i)/2{
                suffix[i] = nums[i];
            }
            else{
                if f.contains_key(&suffix[i+1]) && f[&suffix[i+1]] > (n-i) /2
                {
                    suffix[i] = suffix[i+1];
                }
                else{
                    suffix[i] = -1;
                }
            }
        }

        // println!("{:?}", suffix);

        let mut prefix = vec![0;n];
        let mut f : HashMap<&i32, usize> = HashMap::new();
        for i in (0..n){
            *f.entry(&nums[i]).or_insert(0) +=1 ;
            if f[&nums[i]] > (i+1)/2{
                prefix[i] = nums[i];
            }
            else{
                if f.contains_key(&prefix[i-1]) && f[&prefix[i-1]] > (i+1) /2
                {
                    prefix[i] = prefix[i-1];
                }
                else{
                    prefix[i] = -1;
                }
            }
        }

        // println!("{:?}", prefix);
        
        for i in 0..n-1{
            if prefix[i] == suffix[i+1] && prefix[i]!= -1{
                return i as i32;
            }
        }

        return -1;
    }
}
