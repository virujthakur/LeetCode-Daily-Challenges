class Solution {
public:
    // TC: O(N) SC: O(N)
    vector<int> count;
    vector<int> ans;
    
    void dfs(vector<vector<int>>&  graph, int src, int parent)
    {
        for(auto x: graph[src])
        {
            if(x!=parent)
            {
                dfs(graph,x,src);
                count[src] += count[x];
                ans[src]+= ans[x]+ count[x];
            }
            
        }
        
    }
    
    void dfs2(vector<vector<int>>& graph, int src, int parent , int n)
    {
        for(auto x: graph[src])
        {
            if(x!=parent)
            {
                ans[x]=ans[src] - count[x] + n - count[x];
                dfs2(graph,x,src,n);
            }
            
        }
    }
    
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
      
        vector<vector<int>> graph(n);
        count.resize(n);
        for(int i=0;i<n;i++)
            count[i]=1;
        
        ans.resize(n);
        
        for(int i=0;i<edges.size();i++)
        {
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }
        
        dfs(graph, 0,-1);
        dfs2(graph,0,-1, n);
        return ans;     
        
    }
};
