class Solution:
    #TC: O(5N) SC: O(5)
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_val(num):
            num = list(str(num))
            for i in range(len(num)):
                num[i]= str(mapping[int(num[i])])
            return int(''.join(num))
        
        # for num in nums:
        #     print(num, get_val(num))
        return sorted(nums, key= lambda num: get_val(num))
        
