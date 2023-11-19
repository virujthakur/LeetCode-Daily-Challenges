class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n= len(nums)
        s= set(nums)
        s= list(s)
        s.sort()
        nums.sort()
        
        ans = 0
        freq = {}
        for num in nums :
            if num not in freq:
                freq[num]=1
            else :
                freq[num]+=1
            
        i = 0
        for num in s :
            ans+= freq[num]* i
            i+=1
        return ans
