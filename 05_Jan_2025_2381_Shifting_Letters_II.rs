impl Solution {
    //TC: O(N) SC: O(N)
    pub fn shifting_letters(s: String, shifts: Vec<Vec<i32>>) -> String {
        let n = s.len();
        let mut prefix = vec![0; n+1];

        for shift in shifts{
            let direction = shift[2];
            let end = shift[1] as usize;
            let start = shift[0] as usize;

            if direction == 1{
                prefix[start]+=1;
                prefix[end+1]-=1;
            }
            else{
                prefix[start]-=1;
                prefix[end+1]+=1;
            }
        }

        let mut sum = 0;
        for i in 0..n+1{
            sum+= prefix[i];
            prefix[i] = sum;
        }

        let mut ans = String::from("");
        for (i,c) in s.chars().enumerate(){
            let c_int = (c as u8 - 'a' as u8);
            let c_new_int = ((c_int as i32 + prefix[i] % 26 + 26) % 26) as u8;

            let new_c = (c_new_int as u8 + 'a' as u8) as char;
            ans.push(new_c);
        }

        return ans;
        
    }
}
