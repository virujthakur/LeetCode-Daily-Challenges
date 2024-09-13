class Solution:
    #TC: O(N) SC: O(N)
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xorSum = [0]* n
        s = 0
        for i in range(n):
            s ^= arr[i]
            xorSum[i] = s
            
            
        ans = []
        for l,r in queries:
            if l-1 >=0 :
                ans.append(xorSum[r] ^ xorSum[l-1])
            else:
                ans.append(xorSum[r])
                
        return ans
            
            
