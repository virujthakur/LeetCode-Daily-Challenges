class Solution {
public:
    //TC: O(N) SC: O(N)
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        
        vector<int> indegree(n+1);
        
        vector<vector<int>> graph(n+1);
        
        for(int i=0; i<relations.size(); i++)
        {
            graph[relations[i][0]].push_back(relations[i][1]);
            indegree[relations[i][1]]++;
        }
        
        queue<pair<int,int>> q;
        
        vector<int> completionTime(n+1,0);
        
        for(int i=1; i<=n; i++)
        {
            if(indegree[i]==0)
            {
                q.push({i, time[i-1]});
                completionTime[i]= max(completionTime[i], time[i-1]);
            }
        }
        
        int ans=0;
        
        while(!q.empty())
        {
            auto x= q.front();
            q.pop();
            
            for(auto y: graph[x.first])
            {
                indegree[y]--;
                
                completionTime[y]= max(completionTime[y], x.second+ time[y-1]);
                
                if(indegree[y]== 0)
                    q.push({y, completionTime[y]});
            }
            
            
        }
        
        return *max_element(completionTime.begin(), completionTime.end());
            
        
    }
};
