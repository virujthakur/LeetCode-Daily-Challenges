impl Solution {
    //TC: O(N) SC: O(N)
    pub fn can_be_valid(s: String, locked: String) -> bool {
        let mut st = Vec::new();
        let mut st2 = Vec::new();
        let locked_list : Vec<char> = locked.chars().collect();
        for (i,c) in s.chars().enumerate(){
            if locked_list[i] == '1'{
                if c == '('{
                    st.push((i,c));
                }
                else{
                    if st.pop() == None{
                        if st2.pop() == None{
                            return false;
                        }
                    }
                }
            }
            else{
                st2.push((i,'*'));
            }
        }
        
        while let Some(top)= st.pop(){
            if let Some(top2)= st2.pop(){
                if top2.0 < top.0{
                    return false;
                }
            }
            else{
                return false;
            }
        }

        return st2.len()% 2 == 0;
    }
}
