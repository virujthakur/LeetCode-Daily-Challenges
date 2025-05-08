class Solution:
    #TC: O(M*N*LOG(M*N)) SC: O(M*N)
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        di = [(0,1), (1,0), (0,-1), (-1,0)]
        pq = []

        n, m = len(moveTime), len(moveTime[0])
        visited = [[False]* m for _ in range(n)]

        heapq.heappush(pq, (0,0,0,2))
        while pq:
            cur = heapq.heappop(pq)
            if visited[cur[1]][cur[2]]:
                continue
                
            visited[cur[1]][cur[2]]= True

            if cur[1] == n-1 and cur[2] == m-1:
                return cur[0]

            for d in di:
                newx = cur[1] + d[0]
                newy = cur[2] + d[1]

                if newx >=0 and newy >=0 and newx<n and newy<m and visited[newx][newy]== False:
                    if cur[3] == 1:
                        heapq.heappush(pq, (max(cur[0], moveTime[newx][newy]) + 2, newx, newy,2))
                    else:
                        heapq.heappush(pq, (max(cur[0], moveTime[newx][newy]) + 1, newx, newy,1))

            # print(pq)

        return -1
        
