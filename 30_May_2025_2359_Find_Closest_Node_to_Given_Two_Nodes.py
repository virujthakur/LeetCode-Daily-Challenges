class Solution:
    #TC: O(N) SC: O(N)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]
        for i in range(n):
            if edges[i] > -1:
                graph[i].append(edges[i])

        def bfs(node):
            q = deque()
            visited =[False] * n
            distTo = [10**9] * n
            q.append(node)

            level = 0
            while q:
                sz = len(q)
                for i in range(sz):
                    curNode = q.popleft()
                    visited[curNode] = True
                    distTo[curNode]  = min(distTo[curNode], level)
                    for nbr in graph[curNode]:
                        if visited[nbr] == False:
                            q.append(nbr)
                level+=1

            return distTo

        distTo1, distTo2 = bfs(node1), bfs(node2)
        ansNode = -1
        ansDist = 10**9 + 1
        for i in range(n):
            if ansDist > max(distTo1[i], distTo2[i]) and max(distTo1[i], distTo2[i]) != 10**9:
                ansDist = max(distTo1[i], distTo2[i])
                ansNode = i
            elif ansDist == max(distTo1[i], distTo2[i]):
                ansNode = min(ansNode, i)

        return ansNode
