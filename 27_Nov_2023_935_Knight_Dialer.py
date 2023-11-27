class Solution:
    # TC: N* 10 SC: 10* N
    mod = 10 ** 9 + 7
    d = [(1,2),(-1,2), (-2,1), (-2,-1), (1,-2), (-1,-2), (2,1), (2,-1)]
    graph= {1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [9, 3, 0],
            5: [],
            6: [7, 1, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
           }
    
    dp= [[]]* 5001
    def recur(self, pos, moves):
        if moves == 0 :
            return 1
        
        if self.dp[moves][pos]!=-1 :
            return self.dp[moves][pos]
        
        ways= 0
        for num in self.graph[pos] :
            ways+= self.recur(num, moves-1) % self.mod
            
        self.dp[moves][pos]= ways % self.mod
        return ways % self.mod

    def knightDialer(self, n: int) -> int:
        
        for i in range(5001):
            self.dp[i]= [-1]* 10
        # print(self.dp[5000][0])
        
        ans = 0
        for i in range(10):
            ans+= self.recur(i, n-1)% self.mod
        
        return ans % self.mod
