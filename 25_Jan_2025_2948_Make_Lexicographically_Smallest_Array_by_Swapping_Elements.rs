impl Solution {
    //TC: O(N) SC: O(N)
    pub fn lexicographically_smallest_array(mut nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut pairs: Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &num)| (num, i)).collect();

        // Sort by values (and indices to maintain stability in ties).
        pairs.sort();

        let mut res = vec![0; n];
        let mut st = 0;

        for i in 1..=n {
            if i == n || pairs[i].0 - pairs[i - 1].0 > limit {
                // Sort the indices within the current segment
                let mut indices: Vec<usize> = pairs[st..i].iter().map(|&(_, idx)| idx).collect();
                indices.sort();

                // Assign values lexicographically
                for (k, idx) in indices.iter().enumerate() {
                    res[*idx] = pairs[st + k].0;
                }

                st = i; // Move to the next segment
            }
        }

        res
    }
}
