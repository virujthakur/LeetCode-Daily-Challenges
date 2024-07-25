class Solution:
    #TC: 3NLOGN SC: O(N)
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            idx= random.randint(l, r)
            temp = []
            for i in range(l, r+1):
                if nums[i]< nums[idx]:
                    temp.append(nums[i])
             
            lo = l+ len(temp)
            for i in range(l, r+1):
                if nums[i]== nums[idx]:
                    temp.append(nums[i])
                    
            hi= l+ len(temp)
            ans= (lo+ hi)//2
            
            for i in range(l, r+1):
                    
                if nums[i]> nums[idx]:
                    temp.append(nums[i])
                    
            for i in range(l, r+1):
                nums[i]= temp[i-l]
                
            return ans
        
        def quickSort(l, r):
            if l >=r:
                return
            
            idx = partition(l, r)
            # print(nums, idx, l, r)
            quickSort(l, idx-1)
            quickSort(idx+1, r)
            
        quickSort(0, len(nums)-1)
        
        return nums
                
