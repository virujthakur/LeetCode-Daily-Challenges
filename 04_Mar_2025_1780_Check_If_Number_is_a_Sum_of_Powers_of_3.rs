use std::collections::HashMap;
impl Solution {
    //TC: O(LOG(N)/ LOG(3) * 2^ LOG(N)/ LOG(3))
    pub fn recur(idx: usize, powers: &mut Vec<i32>, target: i32, dp: &mut HashMap<(usize, i32), bool>) -> bool
    {
        if target == 0{
            return true;
        }

        if idx == powers.len(){
            return false;
        }

        if dp.contains_key(&(idx, target)){
            return *dp.get(&(idx,target)).unwrap();
        }

        let ans= Self::recur(idx+1, powers, target - 3i32.pow(idx as u32), dp) || Self::recur(idx+1, powers, target, dp);
        dp.insert((idx, target), ans);
        return ans;
    }

    pub fn check_powers_of_three(n: i32) -> bool {
        let mut powers = vec![0; 16];
        let mut dp : HashMap<(usize,i32), bool> = HashMap::new();
        return Self::recur(0, & mut powers, n, &mut dp);

    }
}
