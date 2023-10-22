class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    int maximumScore(vector<int>& nums, int k) {
        
        int n= nums.size();
        set<pair<int,int>> s1;
        set<pair<int,int>> s2;
        int leftMin= INT_MAX;
        
        for(int i=n-1; i>=k; i--)
        {
            s1.insert({nums[i],i});
            s2.insert({i, nums[i]});
        }
        
        int ans=0;
        for(int i=k; i>=0;i--)
        {
            leftMin= min(nums[i], leftMin);
            
            while(!s1.empty() && s1.rbegin()->first >= leftMin)
            {
                int num= s1.rbegin()->first;
                int idx= s1.rbegin()->second;
                // cout<<leftMin<<" "<<num<< " " <<idx<<endl;
                s1.erase(s1.find({num,idx}));
                s2.erase(s2.find({idx, num}));
            }
            
            if(s1.empty())
                ans= max(ans, leftMin* (n-i));
            else
                ans= max(ans, leftMin * (s2.begin()->first- i));
            // cout<<leftMin<<" "<<ans<<endl;
        }
        
        s1.clear();
        s2.clear();
        set<pair<int,int>, greater<pair<int,int>>> s3;
        
        for(int i=0; i<=k; i++)
        {
            s1.insert({nums[i], i});
            s3.insert({i, nums[i]});
        }
        
        
        int rightMin= INT_MAX;
        
        
        for(int i=k ;i<n; i++)
        {
            rightMin= min(rightMin, nums[i]);
            
            while(!s1.empty() && s1.rbegin()->first >= rightMin)
            {
                int num= s1.rbegin()->first;
                int idx= s1.rbegin()->second;
                // cout<<leftMin<<" "<<num<< " " <<idx<<endl;
                s1.erase(s1.find({num,idx}));
                s3.erase(s3.find({idx, num}));
            }
            
            if(s1.empty())
                ans= max(ans, rightMin* (i+1));
            else
                ans= max(ans, rightMin * (i- s3.begin()->first));
            // cout<<leftMin<<" "<<ans<<endl;
        }
        
        return ans;
        
    }
};
