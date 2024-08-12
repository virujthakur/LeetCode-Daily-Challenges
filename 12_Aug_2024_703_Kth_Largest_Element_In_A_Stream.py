class KthLargest:
    #TC : O(NLOGN) SC: O(N)
    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse= True)
        n = len(nums)
        self.k = k
        
        self.minheap = []
        self.maxheap = []
        i = 0
        while i< k-1:
            heapq.heappush(self.minheap, nums[i])
            i+=1
            
        while i<n:
            heapq.heappush(self.maxheap, -nums[i])
            i+=1

    def add(self, val: int) -> int:
        l = -self.maxheap[0] if len(self.maxheap) > 0 else 0
        r = self.minheap[0] if len(self.minheap) > 0 else 10**9
        
        # print(self.minheap)
        # print(self.maxheap)
        # print(l,r)
        
        if val <= l:
            heapq.heappush(self.maxheap, -val)
        else:
            heapq.heappush(self.minheap, val)
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            
        return -self.maxheap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
