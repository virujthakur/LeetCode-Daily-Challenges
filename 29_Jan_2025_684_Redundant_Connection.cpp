class Solution {
public:
    // TC: O(N) SC: O(N)
    int find(vector<int>& parent, int x)
    {
        if (parent[x] == x){
            return x;
        }

        return parent[x] = find(parent, parent[x]);
    }

    bool unionf(vector<int>& parent, vector<int>& rank, int x, int y)
    {
        int px = find(parent, x);
        int py = find(parent, y);

        if (px != py){
            if (rank[px] > rank[py])
            {
                parent[py] = px;
            }
            else if(rank[px] < rank[py])
            {
                parent[px] = py;
            }
            else{
                parent[py] = px;
                rank[px] +=1;
            }
            return true;
        }
        return false;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> answer;
        vector<int> parent(n+1), rank(n+1,1);
        for(int i=0; i<n; i++)
        {
            parent[i] = i;
        }

        for (auto edge : edges){
            if (!unionf(parent, rank, edge[0], edge[1]))
            {
                answer= edge;
            }
        }

        return answer;
    }
};
