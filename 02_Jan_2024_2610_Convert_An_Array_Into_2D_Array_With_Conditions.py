class Solution:
    #TC: O(N) SC: O(N)
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
            
        ans = []
        while(len(freq) > 0):
            temp= []
            to_delete= []
            for key in freq.keys():
                temp.append(key)
                freq[key]-=1
                if freq[key]==0:
                    to_delete.append(key)
            
            for d in to_delete:
                del freq[d]
            ans.append(temp)
            
        return ans
