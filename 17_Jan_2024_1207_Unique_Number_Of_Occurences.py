class Solution:
    #TC: O(N) SC: O(N)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f= defaultdict(int)
        for num in arr:
            f[num]+=1
        
        return len(f.keys()) == len(set(f.values()))
