class Solution:
    #TC: O(N^3) SC: O(1)
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[j] - arr[i]) <= a and abs(arr[k]- arr[j]) <= b and abs(arr[k]- arr[i]) <= c:
                        ans+=1
        return ans
