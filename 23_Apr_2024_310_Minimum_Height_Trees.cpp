class Solution {
public:
    // TC: O(N) SC: O(N)
    vector<int> res;
    int dfs(vector<vector<int>>& graph, int src, int par, vector<int>& level)
    {
        int h=0;
        for(auto nbr: graph[src])
        {
            if(nbr!= par)
                h= max(h, dfs(graph, nbr, src, level));
        }
        
        return level[src]= h+1;
    }
    
    void dfs2(vector<vector<int>>& graph, int src, int par, vector<int>& level)
    {
        int temp= level[src];
        
        for(auto nbr: graph[src])
        {
            if(nbr!= par)
            {
                int mx=0;
                
                for(auto x: graph[src])
                {
                    if(x== nbr) continue;
                    mx= max(mx, level[x]);
                }
                
                level[src]= mx+1;
                res[nbr]= max(level[nbr]-1, level[src])+ 1;
                dfs2(graph, nbr, src, level);
                
                level[src]= temp;
            }
        }
    }
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        res.resize(n);
        for(auto edge: edges)
        {
            int u= edge[0];
            int v= edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        
        vector<int> level(n, 0);
        int ans= 0;
        ans = dfs(graph, 0, 0, level);
        
        // for(int i=0; i<n; i++)
        //     cout<<level[i]<<" ";
        // cout<<endl;
        
        res[0]= level[0];
        
        dfs2(graph, 0, 0, level);
        
        vector<int> sol;
        
        ans= *min_element(res.begin(), res.end());
        
        for(int i=0; i<n; i++)
            cout<<res[i]<<" ";
        cout<<endl;
        
        for(int i=0; i<n; i++)
        {
            if(res[i]== ans)
                sol.push_back(i);
        }
        
        
        return sol;
        
    }
};
