struct ProductOfNumbers {
    nums: Vec<i32>,
    prefix : Vec<i32> ,
    last_prod : i32 
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ProductOfNumbers {

    fn new() -> Self {
        let mut nums = Vec::new();
        let mut prefix = Vec::new();
        ProductOfNumbers{
            nums : nums,
            prefix : prefix ,
            last_prod : 1,
        }
    }
    
    //TC: O(1) SC: O(N)
    fn add(&mut self, num: i32) {
        self.nums.push(num);
        if num == 0{
            self.last_prod = 1;
            self.nums = Vec::new();
            self.prefix = Vec::new();   
            return;
        }
        else{
            self.last_prod *= num;
        }
        
        self.prefix.push(self.last_prod);
        // println!("{:?}", self.prefix);
    }

    //TC: O(1) SC: O(N)
    
    fn get_product(&self, k: i32) -> i32 {
        let mut ans = self.last_prod;
        let n= self.prefix.len() as i32;

        if self.prefix.len() < k as usize{
            return 0;
        }

        if self.prefix.len() >= (k+1) as usize{ 
            ans/= self.prefix[(n-1-k) as usize];
        }

        ans as i32
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */
