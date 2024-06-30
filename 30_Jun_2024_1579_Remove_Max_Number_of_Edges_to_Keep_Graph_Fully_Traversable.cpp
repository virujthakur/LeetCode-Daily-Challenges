class Solution {
public:
    
    int find(vector<int>& parent, int x)
    {
        if(parent[x]==x) return x;
        else return parent[x]= find(parent, parent[x]);
    }
    
    void unionf(vector<int>& parent, vector<int>& rank, int x, int y)
    {
        int px= find(parent,x);
        int py= find(parent,y);
        
        if(px!=py)
        {
            if(rank[px]< rank[py])
                parent[px]= py;
            else if(rank[px]> rank[py])
                parent[py]= px;
            else
            {
                parent[py]= px;
                rank[px]++;
            }
        }
    }
    
    int returnCount(vector<vector<int>>& edges, int type, vector<int>& parent, vector<int>& rank)
    {
        int count=0;
        
        for(auto edge: edges)
        {
            int t= edge[0];
            int u= edge[1]-1;
            int v= edge[2]-1;
            
            if(t== type)
            {
                int pu = find(parent, u);
                int pv = find(parent, v);
                
                if(pu == pv)
                    count++;
                
                unionf(parent, rank, u, v);
            }
        }
        
        return count;
    }
    
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        
        vector<int> parent(n);
        vector<int> rank(n,1);
        
        for(int i=0;i<n;i++)
            parent[i]=i;
        
        int countBoth= returnCount(edges,3,parent,rank);
        
        vector<int> parent1= parent;
        vector<int> rank1= rank;
        
        int countBob= returnCount(edges,2,parent1,rank1);
        
        vector<int> parent2= parent;
        vector<int> rank2= rank;
        
        int countAlice= returnCount(edges,1,parent2,rank2);
        
        unordered_set<int> parents1;
        for(int i=0;i<n;i++)
            parents1.insert(find(parent1,i));
        
        unordered_set<int> parents2;
        for(int i=0;i<n;i++)
            parents2.insert(find(parent2,i));
        
        
        if(parents1.size()>=2 || parents2.size()>=2) return -1;
        else
        return countBoth + countAlice + countBob;
        
    }
};
