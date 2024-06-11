class Solution:
    #TC: O(N) SC: O(N)
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_s= set(arr2)
        not_present = []
        
        f= defaultdict(int)
        for num in arr1:
            if num in arr2_s:
                f[num]+=1
            else:
                not_present.append(num)
                
        ans =[]
        
        for num in arr2:
            l= [num] * f[num]
            ans+= l
            
        return ans+ sorted(not_present) if len(not_present) > 0 else ans
        
        
        
