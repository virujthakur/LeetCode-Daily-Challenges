class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c= Counter(arr).most_common()[::-1]
        for i,e in enumerate(c):
            t,v= e
            k-= v
            if k<0:
                return len(c)-i
            elif k==0:
                return len(c)-i-1
                
        
        return 0
