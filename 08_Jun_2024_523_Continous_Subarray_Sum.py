class Solution:
    #TC: O(N) SC: O(N)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        f= defaultdict(int)
        f_occ= defaultdict(int)
        
        s = 0
        f[0] =1
        f_occ[0]= -1
        for i,num in enumerate(nums):
            s+= num
            rem= s%k
            if rem in f_occ and i- f_occ[rem] >= 2:
                return True
           
            f[rem] +=1
            if rem not in f_occ:
                f_occ[rem] = i
            
        return False
