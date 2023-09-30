class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    bool find132pattern(vector<int>& nums) {
        
        int n= nums.size();
        if(n<3) return false;
        
        vector<int> suffix(n,-1);
        vector<int> prefix(n,-1);
        
        multiset<pair<int,int>> temp;
        for(int i=n-1; i>=0; i--)
        {
            auto it= temp.lower_bound({nums[i], INT_MIN});
            if(it== temp.begin())
            {
                temp.insert({nums[i], i});
                continue;
            }
            
            it--;
            
            suffix[i]= it->second;
            temp.insert({nums[i], i});
        }
        
        temp.clear();
        
        for(int i=0; i<n; i++)
        {
            if(!temp.empty())
                prefix[i]= temp.begin()->second;
            
            temp.insert({nums[i], i});
        }
        
//         for(int i=0;i<n;i++)
//             cout<<prefix[i]<<" ";
//         cout<<endl;
        
//         for(int i=0;i<n;i++)
//             cout<<suffix[i]<<" ";
//         cout<<endl;
        
        for(int k=1 ;k<n-1; k++)
        {
            int i= prefix[k];
            int j= suffix[k];
            
            if(i>=0 && j>=0 && nums[i] < nums[j])
                return true;
        }
        
        return false;
    }
};
