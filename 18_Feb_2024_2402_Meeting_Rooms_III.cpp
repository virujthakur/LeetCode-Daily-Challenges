class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        
        sort(meetings.begin(),meetings.end());
        
        priority_queue<pair<long long,int>> occupied;
        priority_queue<int> freerooms;
        
        vector<int> meetCount(n);
        
        for(int i=0;i<n;i++) freerooms.push(-i);
        
        for(int i=0;i<meetings.size();i++)
        {
            long long s= meetings[i][0];
            long long e= meetings[i][1];
            
            while(!occupied.empty() && ((-occupied.top().first) <= s))
            {
                int room= occupied.top().second;
                freerooms.push(room);
                occupied.pop();
            }
            
            if(!freerooms.empty())
            {
                int fr= freerooms.top();
                freerooms.pop();
                occupied.push({-e,fr});
                meetCount[-fr]++;
            }
            else
            {
                long long endTime= -occupied.top().first;
                long long newRoom = occupied.top().second;
                int duration = e-s;
                occupied.pop();
                occupied.push({-(endTime+ duration), newRoom});
                meetCount[-newRoom]++;
            }
        }
        
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(meetCount[i]> meetCount[ans])
                ans=i;
        }
        
        return ans;
    }
};
