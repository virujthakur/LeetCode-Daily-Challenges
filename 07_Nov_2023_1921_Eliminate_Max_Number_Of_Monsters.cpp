//TC: O(N) SC:O(N)
class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n= dist.size();
        vector<int> time(n);
        
        for(int i=0; i<n; i++)
        {
            time[i]= ceil((double)dist[i]/ speed[i]);
        }
        
        sort(time.begin(), time.end());
        
        int ans=0;
        for(int i=0; i<n; i++)
        {
            if(time[i] - i > 0)
                ans++;
            else
                return ans;
        }
        
        return ans;
            
    }
};
