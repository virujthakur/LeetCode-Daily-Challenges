use std::cmp::min;
use std::cmp::max;

//TC: O(N) SC: O(1)
impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let mut i =0;
        let mut j= (k-1) as usize;
        let mut ans = blocks.len();
        let blocks : Vec<char> = blocks.chars().collect();
        let mut b =0;
        let mut w =0;

        for _k in i..min(blocks.len(),j){
            if blocks[_k]== 'B'{
                b+=1;
            }
            else{
                w+=1;
            }
        }


        while j < blocks.len(){
            if blocks[j] == 'B'{
                b+=1;
            }
            else{
                w+=1;
            }

            // println!("{},{}", b, w);
            ans = min(ans, max(0,k as usize-b));

            if blocks[i] == 'B'{
                b-=1;
            }
            else{
                w-=1;
            }
            i+=1;
            j+=1;
        }
        ans as i32
    }
}
