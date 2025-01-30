class Solution {
public:
    //TC: O(N * len(Edges)) SC: O(N^3)
    int getNumberOfGroupsForComponent(vector<vector<int>> &adjList, int node,
                                      vector<int> &distances,
                                      vector<int> &visited) {
        // Start with the distance of the current node as the maximum
        int maxNumberOfGroups = distances[node];
        visited[node] = 1;

        // Recursively calculate the maximum for all unvisited neighbors
        for (int neighbor : adjList[node]) {
            if (visited[neighbor] > 0) continue;
            maxNumberOfGroups = max(maxNumberOfGroups,
                                    getNumberOfGroupsForComponent(
                                        adjList, neighbor, distances, visited));
        }
        return maxNumberOfGroups;
    }

    int bfs(vector<vector<int>>& graph, vector<int>& visited, int src)
    {
        queue<int> q;
        q.push(src);
        int level=0;
        visited[src]= 0;
        
        while(!q.empty())
        {
            level++;
            int sz= q.size();
            int color= level%2;
            int prevColor= (level+1)%2;
            
            for(int i=0;i<sz;i++)
            {
                int x= q.front();
                q.pop();
                
                for(auto y: graph[x])
                {
                    if(prevColor== visited[y])
                        return -1;
                    else if(visited[y]==-1)
                    {
                        q.push(y);
                        visited[y]=color;
                    }
                }
                
            }
        }
        
        return level;
    }
    int magnificentSets(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        vector<int> visited(n, -1);
        for(auto edge: edges)
        {
            graph[edge[0]-1].push_back(edge[1]-1);
            graph[edge[1]-1].push_back(edge[0]-1);
        }

        
        for(int i=0; i<n; i++)
        {
            if (visited[i] == -1)
                if (bfs(graph, visited, i) == -1)
                    return -1;
        }

        vector<int> distances(n);
        for(int i=0; i<n; i++)
        {
            visited.clear();
            visited.resize(n, -1);
            distances[i] = bfs(graph, visited, i);
        }

        visited.clear();
        visited.resize(n, -1);
        int res = 0;
        
        for(int i=0 ; i<n ; i++)
        {
            if (visited[i] == -1)
                res+= getNumberOfGroupsForComponent(graph, i, distances, visited);
        }
        
        return res;
    }
};
