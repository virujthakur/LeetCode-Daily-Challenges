import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [[st,en,profit] for st,en,profit in zip(startTime,endTime,profit)]
        jobs.sort()
        
        dp= [-1]* n
        
        def recur(idx):
            if idx == n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            
            ans1 = recur(idx+1)
            # j= idx+1
            j= bisect.bisect_left(jobs,[jobs[idx][1],0], idx+1, n)
            # while j<n and jobs[j][0]< jobs[idx][1]:
            #     j+=1
                
            ans2 = jobs[idx][2]+ recur(j)
            dp[idx]= max(ans1,ans2)
            return dp[idx]
        return recur(0)
