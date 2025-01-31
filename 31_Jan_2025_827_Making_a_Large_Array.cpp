class Solution {
public:
    // TC: O(N^2) SC: O(N^2)
    int dfs(int i, int j, vector<vector<int>>& grid, vector<vector<int>>& visited, vector<pair<int,int>>& directions, int island)
    {
        int n = grid.size();
        int ans = 0;
        visited[i][j] = island;
        for (auto d : directions)
        {
            int newi = i + d.first;
            int newj = j + d.second;

            if (newi >=0 and newj >=0 and newi < n and newj < n and !visited[newi][newj] and grid[newi][newj] == 1)
            {
                ans += dfs(newi, newj, grid, visited, directions, island);
            }
        }

        return 1+ ans;
    }

    int largestIsland(vector<vector<int>>& grid) {
        int n= grid.size();
        vector<vector<int>> visited(n, vector<int> (n, 0));
        vector<pair<int,int>> directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        int res = 0;
        int island = 1;

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(!visited[i][j] and grid[i][j] == 1)
                {
                    res = max(res, dfs(i, j, grid, visited, directions, island));
                    island +=1;
                }
            }
        }

        unordered_map<int, int> island_cnt;
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if (visited[i][j] > 0)
                island_cnt[visited[i][j]] +=1;
            }
        }

        // for(auto x: island_cnt)
        //     cout<<x.first<<" "<<x.second<<endl;


        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(grid[i][j] == 0)
                {
                    // cout<<i <<" "<<j<<endl;
                    int ans = 0;
                    set<int> seen;
                    for( auto d: directions)
                    {
                        int newi = i+ d.first;
                        int newj = j+ d.second;
                        
                        if (newi >=0 and newj >=0 and newi < n and newj < n){
                            if (seen.count(visited[newi][newj])== 0)
                            {
                                ans += island_cnt[visited[newi][newj]];
                                seen.insert(visited[newi][newj]);
                            }
                        }
                    }

                    res = max(res, 1+ ans);
                }
            }
        }

        return res;

    }
};
