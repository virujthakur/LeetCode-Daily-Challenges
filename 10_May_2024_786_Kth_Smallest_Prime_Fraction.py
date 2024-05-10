class Solution:
    #TC: O(N^2) SC: O(1)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        fractions = []
        for i in range(n):
            for j in range(n):
                fractions.append((arr[i]/ arr[j], i, j))
                
        fractions.sort()
        
        return [ arr[fractions[k-1][1]], arr[fractions[k-1][2]] ]
