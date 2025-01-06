impl Solution {
    //TC: O(N^2) SC: O(1)
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let n = boxes.len();
        let mut ans = vec![0;n];

        for (i,c1) in boxes.chars().enumerate(){
            let mut res = 0;
            for (j,c2) in boxes.chars().enumerate(){
                if j == i{
                    continue;
                }
                else{
                    if c2== '1'{
                        res+= (j as i32 -i as i32).abs();
                    }
                }
            }
            ans[i]= res;
        }

        return ans;
    }
}
