class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    int minOperations(vector<int>& nums) {
        
        int n= nums.size();
        set<int> s;
        for(auto num: nums)
            s.insert(num);
        
        vector<int> temp;
        for(auto num : s)
            temp.push_back(num);
        
        int res= n-1; 
        
        for(auto mn: nums)
        {
            auto mnItr= lower_bound(temp.begin(), temp.end(), mn);
            auto mxItr= lower_bound(temp.begin(), temp.end(), mn+ nums.size()-1);
            
            int opsNotNeeded= 0;
            
            if(mxItr!= temp.end() && *mxItr== mn+ nums.size()-1)
                opsNotNeeded = mxItr- mnItr+1;
            else
                opsNotNeeded= mxItr-mnItr;  
            
            // cout<<opsNotNeeded<<endl;
            res= min(res, n- opsNotNeeded);
        }
        
        return res;
        
    }
};
