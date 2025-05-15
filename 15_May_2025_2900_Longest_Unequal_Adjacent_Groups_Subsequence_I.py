class Solution:
    #TC: O(N^2) SC: O(N^2)
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        included = [False] * len(words)
        @cache
        def recur(idx, prev):
            if idx == len(words):
                return 0

            if groups[idx] == prev:
                return recur(idx+1, prev)
            else:
                ans1 = 1+ recur(idx+1, groups[idx])
                ans2 = recur(idx+1, prev)
                
                if ans1 > ans2:
                    included[idx] = True
                
                return max(ans1, ans2)

        
        recur(0, -1)
        ans = [words[_] for _ in range(len(words)) if included[_] == True]
        return ans
