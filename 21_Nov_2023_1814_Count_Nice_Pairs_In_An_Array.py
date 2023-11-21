class Solution:
    # TC : O(N) SC: O(N)
    def reverseNumber(self, num : int):
        new_num = 0
        while(num > 0) :
            new_num += num % 10
            num //= 10
            if num == 0 :
                break
            new_num *= 10
        
        return new_num
    
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        '''
        nums[i]- rev(nums[i]) = nums[j] - rev(nums[j])
        '''
        n = len(nums)
        freq = {}
    
        for i in range(n):
            
            # print(str(nums[i]) + " " + str(self.reverseNumber(nums[i])))
            nums[i] = nums[i] - self.reverseNumber(nums[i])
            
            if(nums[i] not in freq):
                freq[nums[i]] = 1
            else :
                freq[nums[i]]+= 1
        
        ans = 0
        for key,value in freq.items() :
            # print(key)
            # print(value)
            ans += int(((value* (value -1))//2)) % mod
            
        return ans % mod
            
        
        
        
        
