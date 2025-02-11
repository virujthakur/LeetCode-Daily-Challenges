impl Solution {
    // TC: O(N*N) SC: O(1)
    pub fn remove_occurrences(mut s: String, part: String) -> String {
        let mut myS = &mut s;
        while let Some(p) = myS.find(part.as_str()){
            for i in 0..part.len(){
                myS.remove(p);
            }
        }

        return s;
    }
}
