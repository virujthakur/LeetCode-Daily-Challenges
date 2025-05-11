class Solution:
    #TC: O(N) SC: O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n-2):
            if arr[i]%2 and arr[i+1]%2 and arr[i+2]%2:
                return True
        return False
        
