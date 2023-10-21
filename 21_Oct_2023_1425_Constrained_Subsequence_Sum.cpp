class Solution {
public:
    //TC: O(NLOGN) SC: O(K)
    int constrainedSubsetSum(vector<int>& nums, int k) {
        
        int n= nums.size();
        priority_queue<pair<int,int>> pq;
        pq.push({nums[0],0});
        int ans= nums[0];
        
        for(int i=1; i<n; i++)
        {
            while(!pq.empty() && pq.top().second < i-k)
                pq.pop();
            
            int cur= pq.empty() ? 0: max(0, pq.top().first);
            cur+= nums[i];
            ans= max(ans, cur);
            pq.push({cur,i});
        }
          
        return ans;
        
    }
};
