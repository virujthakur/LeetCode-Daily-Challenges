impl Solution {
    //TC: O(N) SC: O(1)
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();
        let mut ans = 0;
        let mut xor1 = 0;
        let mut xor2 = 0;
        for i in 0..n{
            xor1 ^= nums1[i];
        }

        for i in 0..m{
            xor2 ^= nums2[i];
        }

        if m%2 == 1 && n%2 == 1{
            return xor1 ^ xor2;
        }
        else if m%2 == 1{
            return xor1;
        }
        else if n%2 == 1{
            return xor2;
        }
        else{
            return 0;
        }
    }
}
