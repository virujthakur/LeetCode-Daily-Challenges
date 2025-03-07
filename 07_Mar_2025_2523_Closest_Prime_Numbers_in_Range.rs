static mut sieve: [i32; 1_000_001] = [1; 1_000_001];
//TC: O(N* SQRT(N)) SC: O(N)
impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        
        let mut primes = Vec::new();
        unsafe{
                if sieve[0] == 1{
                sieve[0] = 0;
                sieve[1] = 0;

                for i in 2..1_001{
                    if sieve[i] == 0{
                        continue;
                    }

                    let mut j = i*i;
                    while j< 1_000_001{
                        sieve[j] = 0;
                        j+=i;
                    }
                }

            }
        }

        unsafe{

            for i in left..right+1{
                if sieve[i as usize] == 1 {
                    primes.push(i);
                }
            }
        }

        let n= primes.len();
        let mut minDiff = 1_000_000_000;
        let mut ans : Vec<i32> = vec![-1,-1];

        if n > 1
        {
            for i in 0..n-1{
                let j = i+1;
                if primes[j]- primes[i] < minDiff{
                    ans[0] = primes[i] as i32;
                    ans[1] = primes[j] as i32;
                    minDiff = primes[j] - primes[i];
                }
            }
        }

        return ans;
    }
}
