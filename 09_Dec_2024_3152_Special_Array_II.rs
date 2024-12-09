impl Solution {
    //TC: O(N) SC: O(N)
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut res : Vec<bool> = Vec::new();
        let mut pre_computation : Vec<i32> = Vec:: new();
        
        for i in 0..(nums.len()-1){
            if nums[i]%2 != nums[i+1]%2{
                pre_computation.push(1);
            }
            else{
                pre_computation.push(0);
            }
        }
        
        let mut pre_computation_prefix : Vec<i32> = Vec::new();
        pre_computation_prefix.push(0);
        
        let mut s: i32= 0;
        for i in 0..(nums.len()-1){
            s+= pre_computation[i];
            pre_computation_prefix.push(s);
        }
        // println!("{:?}", pre_computation_prefix);
        
        for query in &queries{
            if let [l, r] = &query[..] {
                let ans = pre_computation_prefix[(*r) as usize] - pre_computation_prefix[*l as usize];
                // println!("{}, {}, {}, {}" , ans, r-l, r, l);
                if ans == (r-l){
                    res.push(true);
                }
                else{
                    res.push(false);
                }
            } else {
                panic!("Each query must contain exactly 2 elements.");
            }
        }
        
        res
    }
}
