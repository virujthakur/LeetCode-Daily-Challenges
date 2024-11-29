class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        
        if(grid[0][1]> 1 && grid[1][0] > 1) return -1;
        
        int m= grid.size();
        int n= grid[0].size();
        
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        pq.push({0,0,0});
        
        unordered_map<int,int> timeToReach;
        
        timeToReach[0]=0;
        
        vector<pair<int,int>> dir= {{0,1}, {1,0}, {-1,0}, {0,-1}};
        
        while(!pq.empty())
        {
            vector<int> curNode= pq.top();
            pq.pop();
            int curX= curNode[1];
            int curY= curNode[2];
            int curTime= curNode[0];
            
            for(auto d: dir)
            {
                int newX= curX+ d.first;
                int newY= curY+ d.second;
                int newCode= newX*n + newY;
                
                if(newX>=0 && newY>=0 && newX<m && newY<n)
                {
                    int newTime= grid[newX][newY];
                    if(newTime> (curTime + 1))
                    {
                        if((newTime- curTime) %2 ==0 )
                        {
                            if(timeToReach.find(newCode)== timeToReach.end() || timeToReach[newCode]> newTime+1 )
                            {
                                timeToReach[newCode]= newTime+1;
                                pq.push({newTime+1, newX, newY});
                            }
                        }
                        else
                        {
                            if(timeToReach.find(newCode)== timeToReach.end() || timeToReach[newCode]> newTime )
                            {
                                timeToReach[newCode]= newTime;
                                pq.push({newTime, newX, newY});
                            }
                        }
                    }
                    else
                    {
                        if(timeToReach.find(newCode)== timeToReach.end() || timeToReach[newCode]> curTime+1 )
                        {
                            timeToReach[newCode]= curTime+1;
                            pq.push({curTime+1, newX, newY});
                        }
                    }
                }
            }
            
        }
        
        return timeToReach[m*n-1];
        
    }
};
