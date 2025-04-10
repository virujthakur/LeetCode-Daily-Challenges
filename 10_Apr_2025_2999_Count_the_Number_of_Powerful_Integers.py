class Solution:
    #TC: O(LOG(N)* LIMIT* 2) SC: O(LOG(N)* 2)
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        n1 = len(str(finish)) - len(s)
        start = str(start -1)
        n2 = len(start) - len(s)

        # print(n1, n2)

        @cache
        def recur(idx, n, temp, isSmaller):
            if idx >= n:
                if isSmaller:
                    return 1
                else:
                    return int(int(temp[:idx] + s) <= int(temp))

            en = -1
            if isSmaller == True:
                en = limit
            else:
                en = min(limit, int(temp[idx])- int('0'))

            ans = 0
            for i in range(en+1):
                # print(i, (int(temp[idx])- int('0')))
                ans += recur(idx+1, n, temp, isSmaller | (i < (int(temp[idx])- int('0'))))

            return ans

        h = recur(0, n1, str(finish), False)
        l = recur(0, n2, start, False)
        
        # print(h, l)

        return h-l


