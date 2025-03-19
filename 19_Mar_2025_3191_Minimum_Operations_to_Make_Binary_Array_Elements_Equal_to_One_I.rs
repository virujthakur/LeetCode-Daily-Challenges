impl Solution {
    //TC : O(N) SC: O(N)
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut flipCount = 0;
        let mut ans = 0;
        let mut newNums = vec![0;n];
        for i in 0..n{
            newNums[i] = nums[i];
        }

        let mut offset = vec![0;n+1];

        for i in 0..n{
            let mut curNum = nums[i];
            flipCount -= offset[i];
            if (flipCount) % 2 == 1{
                curNum = curNum ^1;
            }
            
            if i+3 <= n && curNum == 0{
                flipCount +=1;
                ans +=1;
                offset[i+3] +=1;
                curNum = curNum ^1;
            }

            newNums[i] = curNum;
        }

        for i in 0..n{
            if newNums[i] == 0{
                return -1;
            }
        }

        return ans;
    }
}
