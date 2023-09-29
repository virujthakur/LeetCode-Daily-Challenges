class Solution {
public:
    // TC: O(N) SC: O(1)
    bool isMonotonic(vector<int>& nums) {
        
        int n= nums.size();
        
        bool flag1= true;
        
        for(int i=0 ;i<n-1; i++)
            if(nums[i+1] > nums[i])
                flag1= false;
        
        reverse(nums.begin(), nums.end());
        
        bool flag2= true;
        
        for(int i=0 ;i<n-1; i++)
            if(nums[i+1] > nums[i])
                flag2= false;
        
        return flag1 | flag2;
        
    }
};
