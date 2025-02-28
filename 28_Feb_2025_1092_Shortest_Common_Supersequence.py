class Solution:
    #TC: O(N^2) SC: O(N^2)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        transitions = defaultdict(tuple)

        @cache
        def LCS(i, j):
            if i == n and j == m:
                return 0

            if i==n:
                ans = LCS(i, j+1)
                transitions[(i,j+1)]= (i, j)
                return ans
            
            if j==m:
                ans = LCS(i+1, j)
                transitions[(i+1, j)]= (i, j)
                return ans

            ans = 0
            if str1[i] == str2[j]:
                ans = 1+ LCS(i+1, j+1)
                transitions[(i,j)] =(i+1, j+1)
            else:
                ans1 = LCS(i+1, j)
                ans2 = LCS(i, j+1)
                if ans1 >= ans2:
                    transitions[(i,j)] = (i+1, j)
                    ans = ans1
                else:
                    transitions[(i,j)] = (i, j+1)
                    ans = ans2
            return ans

        LCS(0,0)
        # print(transitions)
        i,j = 0, 0

        isLCS1 = [False] * n
        isLCS2 = [False] * m
        while i<n and j<m:
            # print(i, j)
            if i< n and j< m and str1[i] == str2[j]:
                isLCS1[i] = True
                isLCS2[j] = True
            
            if transitions[(i,j)] == ():
                break
            i,j = transitions[i,j]


        # print(isLCS1, isLCS2)
        ans = ''
        
        i, j = 0, 0
        while i<n or j<m:
            while i<n and isLCS1[i]== False:
                ans+= str1[i]
                i+=1
            while j<m and isLCS2[j]== False:
                ans+= str2[j]
                j+=1
            
            if i< n:
                ans+= str1[i]
            elif j<m:
                ans+= str2[j]

            i,j = i+1, j+1

        return ans


