impl Solution {
    // TC: O(N) SC: O(N)
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let n = colors.len();
        let mut _colors = Vec::new(); 
        _colors.extend(colors.clone());
        _colors.extend(colors);
        // println!("{:?}", _colors);

        let mut i =0;
        let mut ans = 0;
        for j in 0..(n+k as usize -1){
            
            if j==i {
                if j-i+1 >=k as usize{
                    // println!("{},{}", i, j);
                    ans+=1;
                }
                continue;
            }
            
            else{
                if _colors[j]== _colors[j-1]{
                    i=j;
                }
            }

            if j-i+1 >=k as usize{
                // println!("{},{}", i, j);
                ans+=1;
            }

        }
        return ans;

    }
}
