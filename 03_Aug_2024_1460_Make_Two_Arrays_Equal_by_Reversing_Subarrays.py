class Solution:
    #TC: O(N) SC: O(N)
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        f1= defaultdict(int)
        f2= defaultdict(int)
        
        for num in arr:
            f1[num]+=1
            
        for num in target:
            f2[num]+=1
            
        return f1 == f2
                
                
