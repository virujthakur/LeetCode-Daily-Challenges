use std::collections::BinaryHeap;
//TC: O(NLOGN) SC: O(N)
impl Solution {
    pub fn find_score(nums: Vec<i32>) -> i64 {
        let mut minHeap = BinaryHeap::new();
        let n = nums.len();
        let mut isMarked = vec![false ; n];
        for i in 0..n{
            minHeap.push((-nums[i] as i64, -(i as i64)));
        }
        
        let mut score = 0;
        while let Some((mut value, mut index)) = minHeap.pop(){
            value = -value;
            index = -index;
            if isMarked[index as usize]{
                continue;
            }
            
            isMarked[index as usize]= true;
            if index -1 >=0{
                isMarked[index as usize -1]= true;
            }
            
            if index +1 < n as i64{
                isMarked[index as usize +1] = true;
            }
            
            score += value;
        }
        
        return score;
    }
}
