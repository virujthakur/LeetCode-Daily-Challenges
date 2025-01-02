impl Solution {
    //TC: O(N) SC: O(N)
    pub fn isVowel(byte : u8) -> bool{
        if byte == b'a' || byte == b'e' || byte == b'i' || byte == b'o' || byte == b'u'{
            return true;
        }
        false
    }

    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = words.len();
        let mut isValid = vec![0;n];
        for i in 0..n{
            let bytes = words[i].as_bytes();
            let m = bytes.len();
            if Self::isVowel(bytes[0]) && Self::isVowel(bytes[m-1]){
                isValid[i] = 1;
            }
        }

        let mut s = 0;
        for i in 0..n{
            s+= isValid[i];
            isValid[i] = s;
        }

        let mut res = Vec::new();
        for q in queries{
            if q[0] == 0{
                res.push(isValid[q[1] as usize]);
            }
            else{
                res.push(isValid[q[1] as usize]- isValid[(q[0] -1) as usize])
            }
        }   
        
        res
    }
}
