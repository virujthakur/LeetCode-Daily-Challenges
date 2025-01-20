use std::collections::HashMap;
impl Solution {
    //TC: O(N) SC: O(N)
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let n = arr.len();
        let mut f : HashMap<i32, Vec<(i32, i32)>>  = HashMap::new();

        let r = mat.len();
        let c = mat[0].len();

        for (i,row) in mat.iter().enumerate(){
            for (j,num) in row.iter().enumerate(){
                f.entry(*num).or_insert(vec![]).push((i as i32,j as i32));
            }
        }

        // println!("{:?}", f);

        let mut rowMap = vec![0;r];
        let mut colMap = vec![0;c];
        
        for (i,num) in arr.iter().enumerate(){
            if let Some(l) = f.get(num){
                for val in l{
                    rowMap[val.0 as usize]+=1;
                    if rowMap[val.0 as usize] == c{
                        return i as i32;
                    }

                    // println!("{:?}", rowMap);
                    colMap[val.1 as usize]+=1;
                    if colMap[val.1 as usize] == r{
                        return i as i32;
                    }

                    // println!("{:?}", colMap);
                    // println!("{},{}", r, c);
                }
            }
        }

        return -1;
    }
}
