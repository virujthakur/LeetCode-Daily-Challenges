class Solution {
public:
    
    // TC: O ((N-1)* LOG(N^2)) SC: O(N^2)
    bool unionf(vector<int>& parent, vector<int>& rank, int x, int y)
    {
        int px= find(parent, x);
        int py= find(parent, y);
        
        if(px!=py)
        {
            if(rank[px]< rank[py])
            {
                parent[px]= parent[py];
            }
            else if(rank[px] > rank[py])
            {
                parent[py]= parent[px];
            }
            else
            {
                parent[py]= parent[px];
                rank[px]++;
            }
            return true;
        }
        
        return false;
    }
    
    int find(vector<int>& parent, int x)
    {
        if(parent[x]==x)
            return x;
        return find(parent, parent[x]);
    }
    
    int manhattan(vector<int>& p1, vector<int>& p2)
    {
        return abs(p1[0]- p2[0]) + abs(p1[1]- p2[1]);
    }
    
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> edges;
        
        for(int i=0;i<n;i++)
        {
            int cost=0;
            for(int j=i+1;j<n;j++)
            {
                edges.push({manhattan(points[i], points[j]), i, j});
                // edges.push_back({manhattan(points[j], points[i]), i, j});
            }
        }
        
        // sort(edges.begin(), edges.end());
        
        vector<int> parent(n);
        vector<int> rank(n,1);
        
        for(int i=0;i<n;i++) parent[i]=i;
        
        int cost=0;
        int count=0;
        while(!edges.empty() && count<n-1)
        {
            auto edge= edges.top();
            edges.pop();
            if(unionf(parent,rank,edge[1], edge[2]))
            {
                cost+= edge[0];
                count++;
            }
        }
        
        return cost;
    }
};