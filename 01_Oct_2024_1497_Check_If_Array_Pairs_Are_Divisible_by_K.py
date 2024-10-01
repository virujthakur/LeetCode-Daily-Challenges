class Solution:
    #TC: O(N+K) SC: O(K)
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = defaultdict(int)
        for num in arr:
            f[num%k]+=1
            
        if f[0]%2 :
            return False
        
        for i in range(1, k//2 + 1):
            if f[i] != f[k-i]:
                return False
            
        return True
            
            
