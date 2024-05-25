class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #TC: O(2^N * N) SC: O(1)
        wordDict = set(wordDict)
        n= len(s)
        ans = []
        
        def recur(idx , path):
            # print(idx,path)
            if idx == n:
                ans.append(' '.join(path))
                return
            
            temp= ''
            for i in range(idx, n):
                temp+= s[i]
                # print(temp)
                if temp in wordDict:
                    newpath = list(path)
                    newpath.append(temp)
                    recur(i+1, newpath)
                    
        recur(0, [])
        return ans
            
