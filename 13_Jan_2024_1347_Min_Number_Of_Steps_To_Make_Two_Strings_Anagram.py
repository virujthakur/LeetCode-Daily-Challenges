class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq= defaultdict(int)
        for c in s:
            freq[c]+=1
        for c in t:
            freq[c]-=1
        
        ans=0
        for key in freq.keys():
            ans+= abs(freq[key])
        
        return ans//2
