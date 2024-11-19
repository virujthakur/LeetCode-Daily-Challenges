class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int n= nums.size();
        int i=0;
        multiset<long long> m;
        set<long long> s;
        long long sum = 0;
        long long ans = 0;
        
        for(int j=0; j<n; j++)
        {
            m.insert(nums[j]);
            s.insert(nums[j]);
            sum += nums[j];
            
            if(j-i+1 == k)
            {
                if(s.size() == k)
                {
                    ans = max(ans, sum);
                }
                
                m.erase(m.find(nums[i]));
                if (m.find(nums[i]) == m.end())
                    s.erase(nums[i]);
                
                sum -= nums[i];
                i+=1;
            }
        }
        
        return ans;
    }
};
