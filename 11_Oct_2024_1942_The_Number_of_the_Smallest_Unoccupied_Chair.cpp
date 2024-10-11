class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        
        set<int> seats;
        for(int i=0; i<1e4+1; i++)
        {
            seats.insert(i);
        }
        
        for(int i=0; i<times.size(); i++)
        {
            times[i].push_back(i);
        }
        
        sort(times.begin(), times.end());
        
        
        set<pair<int,int>> occupied;
        for(int i=0; i<times.size(); i++)
        {
            while(!occupied.empty() && occupied.begin()->first <= times[i][0])
            {
                seats.insert(occupied.begin()->second);
                occupied.erase(occupied.begin());
            }
            
            occupied.insert({times[i][1],*seats.begin()});
            
            if(times[i][2]== targetFriend)
            {
                return *seats.begin();
            }
            
            seats.erase(seats.begin());
        }
        
        return -1;
    }
};
