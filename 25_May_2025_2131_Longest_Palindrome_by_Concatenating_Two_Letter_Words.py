class Solution:
    #TC: O(N) SC: O(N)
    def longestPalindrome(self, words: List[str]) -> int:
        n = len(words)
        f = defaultdict(int)
        for word in words:
            f[word]+=1

        visited = set()
        ans = 0
        mid = 10**9
        mid_k = "??"
        
        for k,v in f.items():
            if k in visited:
                continue

            if k[0] == k[1]:
                if mid > v and v%2:
                    mid = v
                    mid_k = k

                visited.add(k)
            else:
                if k[::-1] in f:
                    ans += min(v, f[k[::-1]])* 4
                    # print(ans)
                    visited.add(k)
                    visited.add(k[::-1])

        print(ans)
        for k,v in f.items():
            if k[0] == k[1]:
                if mid_k == k:
                    ans += v*2
                else:
                    ans += (v- v%2) * 2

        return ans

        
