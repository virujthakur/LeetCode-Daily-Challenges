class Solution:
    #TC: O(NLOGN) SC: O(N)
    def takeCharacters(self, s: str, k: int) -> int:
        # if k ==0:
        #     return 0
        
        n = len(s)
        prefix = [[0]* 3 for _ in range(n)]
        suffix = [[0]* 3 for _ in range(n)]
        
        
        sA, sB, sC = 0,0,0
        for i in range(n):
            
            if s[i] == 'a':
                sA+=1
            elif s[i] == 'b':
                sB+=1
            else:
                sC+=1
                
            prefix[i][0], prefix[i][1], prefix[i][2]= sA, sB, sC
            
        sA, sB, sC = 0,0,0   
        for i in range(n-1, -1, -1):
            if s[i] == 'a':
                sA+=1
            elif s[i] == 'b':
                sB+=1
            else:
                sC+=1
                
            suffix[i][0], suffix[i][1], suffix[i][2]= sA, sB, sC
            
        suffixA = [s[0] for s in suffix]
        suffixB = [s[1] for s in suffix]
        suffixC = [s[2] for s in suffix]
        suffixA.append(0)
        suffixB.append(0)
        suffixC.append(0)
        
        suffixA.reverse()
        suffixB.reverse()
        suffixC.reverse()
        
        prefixA = [0]+ [p[0] for p in prefix]
        prefixB = [0]+ [p[1] for p in prefix]
        prefixC = [0]+ [p[2] for p in prefix]
        
        print(prefixA, prefixB, prefixC, len(prefixA))
            
        ans= 10**9
        # j1 = bisect.bisect_left(suffix, k, 0, n)
        # j2 = bisect.bisect_left(suffix, k, 0, n)
        # j3 = bisect.bisect_left(suffix, k, 0, n)
        # j = max(j1, j2, j3)
        
        for i in range(n+1):
            j1 = bisect.bisect_left(suffixA, k- prefixA[i], 0, n+1-i)
            j2 = bisect.bisect_left(suffixB, k- prefixB[i], 0, n+1-i)
            j3 = bisect.bisect_left(suffixC, k- prefixC[i], 0, n+1-i)
            j = max(j1, j2, j3)
            # print(i, j)
            
            if j == n+1 -i:
                continue
            else:
                ans= min(ans, i+j)
                
        for i in range(n+1):
            j1 = bisect.bisect_left(prefixA, k- suffixA[i], 0, n+1-i)
            j2 = bisect.bisect_left(prefixB, k- suffixB[i], 0, n+1-i)
            j3 = bisect.bisect_left(prefixC, k- suffixC[i], 0, n+1-i)
            j = max(j1, j2, j3)
            # print(i, j)
            
            if j == n+1 -i:
                continue
            else:
                ans= min(ans, i+j)
                
        return ans if ans < 10**9 else -1
            
            
