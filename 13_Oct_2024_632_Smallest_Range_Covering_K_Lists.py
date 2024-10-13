class Solution:
    #TC: O(NLOGN) SC: O(K)
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ansl = -10**5
        ansr = 10**5
        
        pq = []
        heapq.heapify(pq)
        
        r = -10**9
        k = len(nums)
        for i in range(k):
            heapq.heappush(pq, (nums[i][0], 0, i))
            r = max(r, nums[i][0])
        
        while pq:
            l = pq[0][0]
            
            if r-l < ansr - ansl:
                ansr = r
                ansl = l
            elif r-l == ansr- ansl:
                if l < ansl:
                    ansr = r
                    ansl = l
            
            x= heapq.heappop(pq)
            
            if x[1]+1 == len(nums[x[2]]):
                break
            
            r= max(r, nums[x[2]][x[1]+1])
            heapq.heappush(pq, (nums[x[2]][x[1]+1], x[1]+1, x[2]))
            
        return [ansl, ansr]
            
            
            
