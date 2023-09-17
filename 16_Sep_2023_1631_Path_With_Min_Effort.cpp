class Solution {
public:
    vector<vector<int>> dir= {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    int minimumEffortPath(vector<vector<int>>& heights) {
        
        int n= heights.size();
        int m= heights[0].size();
        
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<vector<int>> dist(n, vector<int>(m,INT_MAX));
        
        pq.push({0,0,0});
        
        while(!pq.empty())
        {
            auto cur= pq.top();
            pq.pop();
            int curX= cur[1];
            int curY= cur[2];
            int curCost= cur[0];
            
            if(curX== n-1 && curY== m-1)
                return curCost;
            
            for(auto d: dir)
            {
                int newX= curX+ d[0];
                int newY= curY+ d[1];
                
                if(newX >=0 && newY>=0 && newX<n && newY<m)
                {
                    int newCost= max(curCost, abs(heights[newX][newY]- heights[curX][curY]));
                    if(dist[newX][newY]> newCost)
                    {
                        dist[newX][newY]= newCost;
                        pq.push({newCost, newX, newY});
                    }
                }
            }
        }
        
        return 0;
        
    }
};