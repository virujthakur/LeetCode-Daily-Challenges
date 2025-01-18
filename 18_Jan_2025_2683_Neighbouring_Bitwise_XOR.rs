impl Solution {
    // TC: O(N) SC: O(1)
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        let mut xorSum = 0;
        for d in derived{
            xorSum ^= d;
        }

        return xorSum == 0;
    }
}
