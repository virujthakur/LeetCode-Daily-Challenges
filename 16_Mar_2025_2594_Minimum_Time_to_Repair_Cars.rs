use std::cmp::min;
impl Solution {
    // TC: O(N* SQRT(CARS)* LOG(10^15)) SC: O(1)
    pub fn isValid(ranks: &Vec<i32>, cars: i32, mid: i64) -> bool{
        let n = ranks.len();
        let mut cars_left = cars;
        for i in 0..n{
            let mut ans = 0;
            for j in 0..cars_left+1{
                let time_taken : i64 = j as i64 *j as i64 * ranks[i] as i64;
                if time_taken > mid{
                    break;
                }
                ans = j;
            }
            cars_left -= ans;
        }

        // println!("{}, {}", cars_left, mid);
        return cars_left <= 0;

    }

    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        let mut lo : i64 = 0;
        let mut hi : i64 = 1_000_000_000_000_000;
        let mut ans : i64 = 1_000_000_000_000_000;

        while lo <= hi{
            let mid = lo + (hi-lo) / 2;
            if Self::isValid(&ranks, cars, mid){
                ans = min(ans, mid);
                hi = mid -1;
            }
            else{
                lo = mid +1;
            }
        }

        return ans;
    }
}
