class Solution:
    #TC: O(N) SC: O(N)
    def checkIfExist(self, arr: List[int]) -> bool:
        f = defaultdict(int)
        for num in arr:
            f[num]+=1
            
        for num in arr:
            if num == 0:
                if f[0] > 1:
                    return True
            elif f[2*num] > 0:
                return True
            
        return False
