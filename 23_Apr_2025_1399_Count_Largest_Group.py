class Solution:
    #TC: O(NLOGN) SC: O(N)
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(list)
        for i in range(1,n+1):
            temp = i
            s = 0
            while temp > 0:
                s += temp % 10
                temp //=10

            groups[s].append(temp)

        cnt, mxSize = 0,0
        for (k,v) in groups.items():
            if len(v) > mxSize:
                mxSize = len(v)
                cnt = 1
            elif len(v) == mxSize:
                cnt +=1

        return cnt
