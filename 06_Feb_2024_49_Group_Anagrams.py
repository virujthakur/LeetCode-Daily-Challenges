class Solution:
    #TC: O(N * len(word)* log(len(word)))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f= defaultdict(list)
        for w in strs:
            f[''.join(sorted(w))].append(w)
        
        ans= []
        for v in f.values():
            ans.append(v)
        return ans
