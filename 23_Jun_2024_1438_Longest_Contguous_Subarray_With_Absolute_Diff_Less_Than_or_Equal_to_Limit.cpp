class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    int longestSubarray(vector<int>& nums, int limit) {
        int n= nums.size();
        multiset<int> m;
        
        int i=0;
        int ans = 0;
        for(int j=0; j<n; j++)
        {
            m.insert(nums[j]);
            int mn= *m.begin();
            int mx= *m.rbegin();
            
            while(i<j and mx- mn > limit)
            {
                m.erase(m.find(nums[i]));
                i+=1;
                mn = *m.begin();
                mx = *m.rbegin();
            }
            
            ans = max(ans, j-i+1);
        }
        
        return ans;
    }
};
