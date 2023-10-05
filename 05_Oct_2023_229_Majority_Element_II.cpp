class Solution {
public:
    //TC: O(N) SC: O(1)
    vector<int> majorityElement(vector<int>& nums) {
        
        unordered_map<int,int> cnt;
        int n= nums.size();
        
        for(int i=0; i<nums.size(); i++)
        {
            if(cnt.size()<2)
                cnt[nums[i]]++;
            else
            {
                if(cnt.count(nums[i]))
                   cnt[nums[i]]++;
                else
                {
                    vector<int> toerase;
                    for(auto x: cnt)
                    {
                        cnt[x.first]--;
                        if(cnt[x.first]==0)
                            toerase.push_back(x.first);
                    }
                    
                    for(auto x: toerase)
                    {
                        cnt.erase(x);
                    }
                }
            }
                

        }
        
        unordered_map<int,int> f;
        
        for(int i=0; i<n;i++)
        {
            for(auto x: cnt)
            {
                if(nums[i]== x.first)
                    f[nums[i]]++;
            }
        }
        
        vector<int> ans;
        
        for(auto x: cnt)
        {
            if(f[x.first]> (n/3))
                ans.push_back(x.first);
        }
        
        return ans;
    }
};
