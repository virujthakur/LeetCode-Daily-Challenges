class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    int minOperations(vector<int>& nums, int x) {
        
        int n= nums.size();
        vector<long long> prefix(n);
        vector<long long> suffix(n);
        
        long long sum=0;
        for(int i=0;i<n;i++)
        {
            sum+= nums[i];
            prefix[i]= sum;
        }
        
        sum=0;
        
        for(int i=n-1; i>=0; i--)
        {
            sum+= nums[i];
            suffix[i]= sum;
        }
        
        int ans= n+1;
        int idx= lower_bound(suffix.begin(), suffix.end(), x, greater<int>()) - suffix.begin();
        
        if(idx< n && suffix[idx]==x)
            ans= n-idx;
        
        for(int i=0;i<n;i++)
        {
            if(prefix[i]> x)
                break;
            
            int idx= lower_bound(suffix.begin()+i+1, suffix.end(), x-prefix[i], greater<int>()) - suffix.begin();
            // cout<<i<<" "<<idx<<endl;
            if(idx<n && suffix[idx]== x- prefix[i])
                ans= min(ans, i+1 + n- idx);
            else if(idx==n && prefix[i]==x)
                ans= min(ans,i+1);
        }
        
        return ans==n+1? -1: ans;
        
    }
};
