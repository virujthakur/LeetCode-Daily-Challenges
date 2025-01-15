impl Solution {
    //TC: O(32) SC: O(32)
    pub fn get_bits(num : i32) -> Vec<i32>{
        let mut bits = Vec::new();
        let mut temp = num;
        while temp > 0{
            bits.push(temp%2);
            temp /=2;
        }

        while bits.len() < 32{
            bits.push(0);
        }

        bits.reverse();
        return bits;
    }
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        
        let mut bits1 = Self::get_bits(num1);
        let mut bits2 = Self::get_bits(num2);
        let mut bits3 = vec![0; 32];

        let mut set_bits = 0;
        for i in 0..32{
            if bits2[i] == 1{
                set_bits +=1;
            }
        }

        for i in 0..32{
            if set_bits == 0{
                break;
            }

            if bits1[i] == 1{
                bits3[i] = 1;
                set_bits -=1;
            }
        }

        let mut ans= 0;
        bits3.reverse();
        let mut mul = 1;

        for i in 0..32{
            if bits3[i] == 0 && set_bits > 0{
                set_bits -=1;
                bits3[i] =1 ;
            }
        }

        for i in 0..32{
            if bits3[i] ==1{
                ans+= mul;
            }

            mul*=2;
        }
        
        return ans;
    }
}
