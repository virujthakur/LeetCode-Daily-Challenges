class Solution:
    #TC : O(NLOGN) SC: O(1)
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort()
        
        prefixMax = []
        mxBeauty = 0
        for item in items:
            mxBeauty = max(mxBeauty, item[1])
            prefixMax.append(mxBeauty)
         
        # print(items)
        ans = []
        for q in queries:
            idx = bisect.bisect_left(items, [q+1, -1], 0, n)
            
            if idx < n and items[idx][0] == q:
                ans.append(prefixMax[idx])
            elif idx > 0 and items[idx-1][0] <= q:
                ans.append(prefixMax[idx-1])
            else:
                ans.append(0)
                
        return ans
            
