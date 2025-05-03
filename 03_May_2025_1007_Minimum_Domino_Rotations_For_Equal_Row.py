class Solution:
    #TC: O(6N) SC: O(1)
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = n+1

        for i in range(1, 7):
            cnt_tops, cnt_bottoms, cnt_both = 0,0,0
            for j in range(n):
                if tops[j] == i and bottoms[j] == i:
                    cnt_both +=1
                elif tops[j] == i :
                    cnt_tops +=1
                elif bottoms[j] == i:
                    cnt_bottoms +=1

            if cnt_tops + cnt_bottoms + cnt_both == n:
                ans = min(cnt_tops, cnt_bottoms)
                
        return ans if ans < n+1 else -1
