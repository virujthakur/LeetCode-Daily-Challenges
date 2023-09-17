class Solution {
public:
    //TC: O(N * 2^N * N) SC: O(N* 2^N)  simultaneous bfs from every node
    int shortestPathLength(vector<vector<int>>& graph) {
        
        int n= graph.size();
        
        queue<vector<int>> q;
        int all= (1<<n) -1;
        set<pair<int,int>> visited;
        
        for(int i=0;i<n;i++)
        {
            visited.insert({1<<i,0});
            q.push({i, 1<<i, 0});
        }
        
        while(!q.empty())
        {
            auto cur= q.front();
            q.pop();
            
            int curNode= cur[0];
            int curMask= cur[1];
            int curCost= cur[2];
            
            if(curMask == all)
                return curCost;
            
            for(auto x: graph[curNode])
            {
                int newMask= curMask | (1<<x);
                if(!visited.count({x,newMask}))
                {
                    q.push({x, newMask, curCost+1});
                    visited.insert({x,newMask});
                }
            }
        }
        
        return 0;
        
    }
};