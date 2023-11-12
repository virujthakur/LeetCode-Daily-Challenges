class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        
        unordered_map<int, vector<int>> stopToBuses;
        int n= routes.size();
        for(int i=0; i<n; i++)
        {
            for(auto stop: routes[i])
            {
                stopToBuses[stop].push_back(i);
            }
        }
        
        int buses= 0;
        queue<int> q;
        
        unordered_set<int> visited;
        unordered_set<int> bvisited;
        
        q.push(source);
        visited.insert(source);
        if(source== target) return buses;
        
        while(!q.empty())
        {
            int sz= q.size();
            for(int i=0; i<sz; i++)
            {
                int curStop= q.front();
                q.pop();
                
                for(auto bus: stopToBuses[curStop])
                {
                    if(!bvisited.count(bus))
                    {
                        for(auto stop: routes[bus])
                        {
                            if(stop== target)
                                return buses+1;
                            if(!visited.count(stop))
                            {
                                q.push(stop);
                                visited.insert(stop);
                            }
                        }

                        bvisited.insert(bus);
                    }
                
                }
            }
            buses++;
        }
        
        return -1;
            
        
    }
};
