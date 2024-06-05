class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #TC: O(N*M) + O(26*N) SC: O(N)
        f_list = []
        for word in words:
            f= defaultdict(int)
            for c in word:
                f[c]+=1
                
            f_list.append(f)
                
        ans =[]    
        for c in range(ord('a'), ord('z')+1):
            mn= 10**9
            for f in f_list:
                # print(f[chr(c)])
                mn= min(mn, f[chr(c)])
            
            for i in range(mn):
                ans.append(chr(c))
            
        return ans
                
