class Solution:
    # TC : O(N*M) SC : O(1)
    def numberOfBeams(self, bank: List[str]) -> int:
        n= len(bank)
        m= len(bank[0])
        
        ans= 0
        prev= 0
        for i in range(n):
            cur= 0
            for j in range(m):
                if bank[i][j] == '1':
                    cur+=1
           # print(cur,prev)
            ans+= (cur* prev)
            if cur > 0:
                prev = cur 

        
        return ans 
